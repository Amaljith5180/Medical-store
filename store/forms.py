from django import forms
from .models import Medicine
from django.contrib.auth.forms import UserCreationForm


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'stock','date']

class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        # Remove help_text for specific fields
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None



     
