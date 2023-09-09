import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Crea tres usuarios con RUTs específicos, contraseñas y datos aleatorios de dinero'

    def handle(self, *args, **kwargs):
        # Datos de los tres usuarios
        user_data = [
            {
                'rut': '12345678',
                'password': 'demo1234',
            },
            {
                'rut': '87654321',
                'password': 'demo1234',
            },
            {
                'rut': '12348765',
                'password': 'demo1234',
            },
        ]

        for data in user_data:
            try:
                User.objects.create_user(
                    username=data['rut'],
                    rut=data['rut'],
                    password=data['password'],
                    account_number=random.randint(10000000000, 9999999999999),
                    countable_balance=random.uniform(1000.00, 10000.99),  # Genera un número aleatorio entre 1000 y 10000
                    balance_available_current_account=random.uniform(500.00, 5000.99),  # Genera un número aleatorio entre 500 y 5000
                    available_credit_line_balance=random.uniform(2000.00, 20000.99),  # Genera un número aleatorio entre 2000 y 20000
                    total_charges=random.uniform(500.00, 5000.99),  # Genera un número aleatorio entre 500 y 5000
                    total_abonos=random.uniform(2000.00, 20000.99),  # Genera un número aleatorio entre 2000 y 20000
                )

            except InterruptedError:
                # En caso de colisión de clave única (rut), simplemente omite el usuario duplicado
                pass

        self.stdout.write(self.style.SUCCESS('Se crearon tres usuarios con los RUTs, contraseñas y datos aleatorios especificados.'))
