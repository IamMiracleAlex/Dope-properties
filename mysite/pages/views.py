from django.shortcuts import render
from properties.models import Property
from realtors.models import Realtor
from properties.choices import state_choices, bedroom_choices, price_choices


def index(request):
    # pylint: disable = no-member
    properties = Property.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'properties': properties,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')  # get realors # pylint: disable = no-member
    mvp_realtors = Realtor.objects.filter(is_mvp=True)  # mvp realtors # pylint: disable = no-member
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)
