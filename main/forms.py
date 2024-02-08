from django import forms
from .models import ContactProfile


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True,
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'Full Name'
                           }))
    email = forms.EmailField(max_length=254, required=True,
                             widget=forms.TextInput(attrs={
                                 'placeholder': 'Email',
                                 'class': 'form-control',
                             }))
    message = forms.CharField(max_length=100, required=True,
                              widget=forms.Textarea(attrs={
                                  'placeholder': '*Message..',
                                  'rows': 6
                              }))

    class Meta:
        model = ContactProfile
        fields = ('name', 'email', 'message')

    def clean_email(self):
        email = self.cleaned_data['email']
        if not "@" in email:
            raise forms.ValidationError("Email address is not valid")
        return email

    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message) < 10:
            raise forms.ValidationError("Message is too short")
        return message
