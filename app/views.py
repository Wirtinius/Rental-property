from .models import Property
from django.shortcuts import render
from django.db.models import Q

def properties(request):
    query = request.GET.get('q')
    if query is None:
        properties = Property.objects.all()
    else:

        properties = Property.objects.filter(
            Q(location_area__icontains=query) |
            Q(location_city__icontains=query) |
            Q(location_pincode__icontains=query)
        )
    return render(request, 'property_list.html', {'properties': properties})

def property_search(request):
    return render(request, 'property_search.html', {'properties': properties})

def property_detail(request, id):
    property = Property.objects.get(id=id)
    return render(request, 'property_detail.html', {'property': property})
