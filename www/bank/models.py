from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth import authenticate

# Create your models here.
STATUS_USUARIO = (
    ('BLOCKED', 'Bloqueado'),
    ('ACTIVE', 'Activo')
    )


class Usuario(AbstractUser):
    rut = models.CharField(max_length=8, null=True, unique=True, verbose_name='Rut')
    account_number = models.PositiveIntegerField(null=True, verbose_name='Numero de cuenta')
    countable_balance = models.DecimalField( null=True, decimal_places=2, max_digits=10)
    balance_available_current_account = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    available_credit_line_balance = models.DecimalField(null=True, decimal_places=2, max_digits=10)
    total_charges = models.DecimalField( null=True, decimal_places=2, max_digits=10)
    status = models.CharField(choices=STATUS_USUARIO, default='ACTIVE', max_length=64)
    failed_login_attempts = models.PositiveIntegerField(default=0,)
    total_abonos = models.DecimalField(null=True, decimal_places=2, max_digits=10) # No se consiguio traduccion literal

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'