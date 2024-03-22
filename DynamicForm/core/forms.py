from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Форма в которой указывается поле имени и телефона контакта.
    """
    class Meta:
        model = Contact
        fields = ['name', 'phone_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }
