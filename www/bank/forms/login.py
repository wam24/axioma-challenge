from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()
__all__ = ['CustomAuthenticationForm']


class CustomAuthenticationForm(AuthenticationForm):
    rut = forms.CharField(max_length=254,
                          widget=forms.TextInput(attrs={'autofocus': True}), )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = False

    def clean(self):


        rut = self.cleaned_data.get('rut')
        password = self.cleaned_data.get('password')

        if rut and password:
            user = User.objects.filter(Q(rut=rut) | Q(username=rut))

            if user.exists():
                user = user.first()
                self.cleaned_data['username'] = user.username
                if user.status == 'BLOCKED':
                    self.add_error('rut',
                                   'Usuario bloqueado, comuniquese con el administrador')
                if not user.check_password(password):
                    user.failed_login_attempts += 1
                    user.save()
                    if user.failed_login_attempts < 2:
                        self.add_error('password',
                                       'Credenciales inválidas. Intentos fallidos: ' + str(user.failed_login_attempts))
                    else:
                        self.add_error('password',
                                       'Credenciales inválidas. Un intentos fallido más y usuario sera bloqueado')
                    if user.failed_login_attempts >= 3:
                        user.status = 'BLOCKED'
                        user.save()
            else:
                self.add_error('rut', 'Credenciales inválidas')

        cleaned_data = super().clean()

        return cleaned_data
