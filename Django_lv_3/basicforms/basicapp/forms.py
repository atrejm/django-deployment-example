from django import forms
from .models import PersonModel

from django.core import validators

class FormName(forms.ModelForm):
    # name = forms.CharField()
    # email = forms.EmailField()
    # desc = forms.CharField(widget=forms.Textarea)
    

    class Meta:
        model = PersonModel
        fields = "__all__"

    # def clean(self):
    #     all_clean_data = super().clean()
    #     email = all_clean_data.get('email')
    #     vmail = all_clean_data.get('verify_email')
        
    #     if email != vmail:
    #         raise forms.ValidationError("Emails don't match")