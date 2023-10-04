from django import forms
from captcha.fields import ReCaptchaField, ReCaptchaV2Checkbox


class ContactForm(forms.Form):
    email = forms.EmailField(label="Email")
    subject = forms.CharField(max_length=100, label="Objet", help_text="100 caractères max")
    message = forms.CharField(max_length=5000, label="Message", help_text="5000 caractères max", widget=forms.Textarea)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
