from django import forms
from .models import Organization

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['phone', 'area']

    def clean(self):
        cleaned_data = super().clean()
        phone = cleaned_data.get('phone')
        address = cleaned_data.get('address')
        area = cleaned_data.get('area')

        if phone:
            if not phone.isdigit():
                self.add_error('phone', 'O telefone deve conter apenas dígitos.')
            elif len(phone) < 10:
                self.add_error('phone', 'O telefone deve ter no mínimo 10 dígitos.')

        if not area:
            self.add_error('area', 'A área é obrigatória.')
            
        return cleaned_data
