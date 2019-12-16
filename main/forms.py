from django import forms

from .models import Type, Manufacturer

class ManufacturerForm(forms.ModelForm):
    super_category = forms.ModelChoiceField(
        queryset=Type.objects.all(), empty_label=None, label='Тип устройства', required=True
    )

    class Meta:
        model = Manufacturer
        fields = '__all__'