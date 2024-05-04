from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'company_name', 'phone_number', 'email', 'service_type', 'message']


    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Ad'})
        self.fields['company_name'].widget.attrs.update({'placeholder': 'Şirkətin adı'})
        self.fields['phone_number'].widget.attrs.update({
            'placeholder': '(_ _) _ _ _-_ _-_ _',
            'class': 'phone-mask',
            'style': 'padding-left: 3.2rem; font-size: 14px',
        })
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['service_type'].widget.attrs.update({
            'class': 'select_2',
        })
        self.fields['message'].widget.attrs.update({
            'placeholder': 'Mesaj (tədbirin başlama, bitmə vaxtlarını və saatı qeyd edin)',
            'rows': 7
            })