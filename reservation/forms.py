from django import forms
from .models import Client, Room


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'client_name': forms.TextInput(attrs={'class': 'form-control'}),
            'client_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'client_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'client_address': forms.TextInput(attrs={'class': 'form-control'}),
            'client_country': forms.TextInput(attrs={'class': 'form-control'}),
            'client_city': forms.TextInput(attrs={'class': 'form-control'}),
            'client_zip': forms.TextInput(attrs={'class': 'form-control'}),
        }

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        widgets = {
            'room_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'room_type': forms.TextInput(attrs={'class': 'form-control'}),
            'room_status': forms.Select(choices=(('Available', 'Available'), ('Booked', 'Booked')), attrs={'class': 'form-control'}),
            'room_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'room_description': forms.Textarea(attrs={'class': 'form-control'}),
            'client': forms.Select(attrs={'class': 'form-control'}),
        }
