from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail


def contact(request):
    if request.method == "POST":
        property_id = request.POST['property_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        prop = request.POST['prop']
        # realtor_email = request.POST['realtor_email']

        # check if users has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            # pylint: disable = no-member
            has_contacted = Contact.objects.filter(property_id=property_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "You have already made an inquiry for this property")
                return redirect('/properties/'+property_id)


        contact = Contact(property_id=property_id, name=name, email=email, phone=phone, message=message,                    user_id=user_id, prop=prop)
        contact.save()

        # Send mail to the reactor
        # send_mail(
        #     "Property Inquiry",  # mail subject
        #     f"There has been an inquiry for {prop}, log in to the admin panel for more info", # body
        #     "collinsalex50@gmail.com", # sender email
        #     [realtor_email, 'alexandcollins@yahoo.com'], # recipient emails
        #     fail_silently=False # raise erros if there's a problem
        # )
        messages.success(request, "Your inquiry was submitted successfully")
        return redirect('/properties/'+property_id)
        


