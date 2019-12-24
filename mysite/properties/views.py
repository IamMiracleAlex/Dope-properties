from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import state_choices, bedroom_choices, price_choices

from .models import Property


def properties(request):
    # pylint: disable = no-member
    properties = Property.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(properties, 6)
    page = request.GET.get('page')
    paged_properties = paginator.get_page(page)

    context = {
        'properties': paged_properties
    }
    return render(request, 'properties/properties.html', context) 

def property_(request, property_id):
    prop = get_object_or_404(Property, id=property_id)
    context = {
        'prop' : prop
    }
    return render(request, 'properties/property.html', context) 

def search(request):
    # pylint: disable = no-member
    query_list = Property.objects.order_by('-list_date') 

    # keywords
    if 'keywords' in request.POST:   # checks for keyword search
        keywords = request.POST['keywords']  
        if keywords:     # makes sure keyword is not an empty string
            # searches if the keyword is contained in the field description (case insensitive)
            query_list = query_list.filter(description__icontains=keywords) 

    # city
    if 'city' in request.POST:
        city = request.POST['city']
        if city:
            query_list = query_list.filter(city__iexact=city) # case insensitive exact search

    # state
    if 'state' in request.POST:
        state = request.POST['state']
        if state:
            query_list = query_list.filter(state__iexact=state)

    # bedrooms
    if 'bedrooms' in request.POST:
        bedrooms = request.POST['bedrooms']
        if bedrooms:
            query_list = query_list.filter(bedrooms__lte=bedrooms)  # less than or equal to search 

    # price
    if 'price' in request.POST:
        price = request.POST['price']
        if price:
            query_list = query_list.filter(price__lte=price)             

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'properties': query_list,
        'values': request.POST
    }
    return render(request, 'properties/search.html', context) 


