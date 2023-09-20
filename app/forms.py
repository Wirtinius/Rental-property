from django import forms
from .models import VisitRequest, Property, PropertyPhoto
from django.forms import inlineformset_factory

class VisitRequestForm(forms.ModelForm):
    class Meta:
        model = VisitRequest
        fields = ['name', 'mobile_number', 'email', 'message']


class PropertyPhotoForm(forms.ModelForm):
    class Meta:
        model = PropertyPhoto
        fields = ['image']


PropertyPhotoFormSet = inlineformset_factory(Property, PropertyPhoto, form=PropertyPhotoForm, extra=1, can_delete=True)
class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'

from django import forms