from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import django.forms as forms
from .models import Perfil, Direccion
#formulario base con clases de BS
class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, 
        required=True, 
    )
    last_name = forms.CharField(
        max_length=30, 
        required=True, 
    )
    email = forms.EmailField(
        required=True
        )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(),
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }

class PerfilModelForm(BaseForm):
    class Meta:
        model = Perfil
        fields = ['nombre2','apellido2','rut','telefono','tipo_usuario']
        exclude =['usuario','direccion']
        labels = {
            'nombre2': 'Segundo Nombre',
            'apellido2': 'Segundo Apellido',
            'rut': 'RUT',
        }
class DireccionModelForm(BaseForm):
    class Meta:
        model = Direccion
        fields = ['comuna', 'calle', 'numero', 'piso', 'departamento']
