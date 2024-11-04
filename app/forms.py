from django import forms
from phonenumber_field.formfields import PhoneNumberField
from layanan.models import Report

class ReportForm(forms.Form):
    name=forms.CharField(required=True)
    email=forms.EmailField(required=True)
    phonenumber=PhoneNumberField(region="ID")
    title=forms.CharField(required=True)
    description=forms.TextInput(required=True)