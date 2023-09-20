from .models import Property
from django.shortcuts import render
from django.db.models import Q
from .forms import VisitRequestForm, PropertyForm, PropertyPhotoFormSet
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .models import VisitRequest

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


def request_visit(request, id):
    property = get_object_or_404(Property, id=id)
    if request.method == 'POST':
        form = VisitRequestForm(request.POST)
        if form.is_valid():
            visit_request = form.save(commit=False)
            visit_request.property = property
            visit_request.save()
    else:
        form = VisitRequestForm()
    return render(request, 'request_visit.html', {'property': property, 'form': form})


def approve_visit_requests(request):
    if not request.user.is_staff:
        return redirect('home')
    pending_requests = VisitRequest.objects.filter(status='pending')
    return render(request, 'approve_visit_requests.html', {'pending_requests': pending_requests})


def approve_request(request, request_id):
    action = request.GET.get('action')

    visit_request = get_object_or_404(VisitRequest, id=request_id)

    if action == 'approve':
        visit_request.status = 'accepted'
    elif action == 'decline':
        visit_request.status = 'declined'

    visit_request.save()

    return redirect('approve_visit_requests')


def add_property(request):
    if request.method == 'POST':
        property_form = PropertyForm(request.POST, request.FILES)
        photo_formset = PropertyPhotoFormSet(request.POST, request.FILES, instance=Property())

        if property_form.is_valid() and photo_formset.is_valid():
            property = property_form.save()
            photo_formset.instance = property
            photo_formset.save()

            return redirect('property_detail', id=property.id)
    else:
        property_form = PropertyForm()
        photo_formset = PropertyPhotoFormSet(instance=Property())

    return render(request, 'add_property.html', {'property_form': property_form, 'photo_formset': photo_formset})

