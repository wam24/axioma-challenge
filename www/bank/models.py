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
    countable_balance = models.DecimalField(null=True, decimal_places=2, max_digits=10, verbose_name='Saldo contable')
    balance_available_current_account = models.DecimalField(null=True, decimal_places=2, max_digits=10,
                                                            verbose_name='Saldo disponible cuenta corriente')
    available_credit_line_balance = models.DecimalField(null=True, decimal_places=2, max_digits=10,
                                                        verbose_name='Saldo disponible línea de credito')
    total_charges = models.DecimalField(null=True, decimal_places=2, max_digits=10, verbose_name='Total cargos')
    status = models.CharField(choices=STATUS_USUARIO, default='ACTIVE', max_length=64, verbose_name='Estado')
    failed_login_attempts = models.PositiveIntegerField(default=0, verbose_name='Intentos fallidos al iniciar sesión')
    total_abonos = models.DecimalField(null=True, decimal_places=2, max_digits=10, verbose_name='Total abonos')  # No se consiguio traduccion literal

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
