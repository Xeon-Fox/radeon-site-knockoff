from django import forms
from .models import Gpu

class GpuForm(forms.ModelForm):
    class Meta:
        model = Gpu
        fields = ["title", "price", "release_date", "image", "description"]
        widgets = {"release_date": forms.DateInput(attrs={"type": "date"})}

class CreateUpdateGpuForm(forms.ModelForm):
    class Meta:
        model = Gpu
        fields = ["title", "price", "release_date", "image", "description"]