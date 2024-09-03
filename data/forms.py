from django import forms

class ProfileForm(forms.Form):
    user= forms.HiddenInput()
    bio=forms.CharField(max_length=255)
    profile_picture= forms.ImageField()
        
class ContactForm(forms.Form):
    user= forms.HiddenInput()
    contact_name= forms.CharField()
    contac_email= forms.EmailField()
    phone= forms.CharField()
    message=forms.CharField()