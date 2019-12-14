from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from contacts.models import Contact


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username is not available')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.error(request, 'This email is in use')
                return redirect('register')

            else:  # looks good
                user = User.objects.create_user(first_name=first_name, last_name=last_name,
                                                username=username, email=email, password=password)
                ''' to login user at once'''
                # auth.login(request, user)
                # messages.success(request, "You've been logged in successfully")
                # return redirect('index')
                ''' to make user login manually'''
                user.save()
                messages.success(
                    request, 'Success! You are registered and can now login')
                return redirect('login')

        messages.error(request, "Passwords do not match")
        return redirect('register')

    return render(request, 'accounts/register.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.info(request, "You're now logged out")
        return redirect('index')


@login_required
def dashboard(request):
    # pylint: disable = no-member
    user_contacts = Contact.objects.order_by(
        '-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)
