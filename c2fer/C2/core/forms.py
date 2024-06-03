from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Propuesta

class CustomAdminUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff', 'is_superuser')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True


class RegistroUsuarioForm(UserCreationForm):
    is_profesor = forms.BooleanField(required=False)
    is_estudiante = forms.BooleanField(required=False)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('nombre', 'email', 'password1', 'password2', 'is_profesor', 'is_estudiante')

    def clean(self):
        cleaned_data = super().clean()
        is_profesor = cleaned_data.get("is_profesor")
        is_estudiante = cleaned_data.get("is_estudiante")
        if is_profesor and is_estudiante:
            raise forms.ValidationError("Un usuario no puede ser profesor y estudiante al mismo tiempo.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = False
        user.is_active = True
        if commit:
            user.save()
        return user

from django import forms
from .models import Propuesta

class PropuestaForm(forms.ModelForm):
    class Meta:
        model = Propuesta
        fields = ['titulo', 'descripcion']