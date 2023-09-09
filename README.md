# axioma-challenge


Formulario

## Requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- Python (versión  >= 3.9)
- Virtualenv (opcional pero recomendado)

## Instalación

1. Clona este repositorio en tu máquina local:

```bash
   git clone https://github.com/wam24/axioma-challenge.git
   ```
    
2. Ve al directorio del proyecto:

```bash
    cd axioma-challenge
```

3. Crea y activa un entorno virtual (opcional pero recomendado):

```bash
  virtualenv venv 
  source venv/bin/activate
```

4. Instala las dependencias del proyecto:

```bash
  pip install -r requirements.txt

```
5. Ejecutar migraciones:
```bash
  python www/manage.py migrate

```
6. Ejecutar comando para demo:
```bash
  python www/manage.py fill_users
  
```
El comando creará 3 usuarios para pruebas
```js
    [
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
```
## Ejecución

Una vez que hayas realizado la instalación, puedes ejecutar el proyecto con el siguiente comando:

```bash
  python manage.py runserver
```

Cuando ingrese a la aplicación podrá observar el formulario de inicio de sesión

## Docker 
Existen un Dockerfile para realizar pruebas, esta usando alphine

Las variables necesarias son las siguientes:
```bash
APP_ADMIN_USER: Usuario administrador
APP_ADMIN_PASSWORD: Contraseña de usuario administrador
DOMAIN_NAME: Dominio

Ejemplo de construccion:  docker build --build-arg APP_ADMIN_USER=admin --build-arg APP_ADMIN_PASSWORD=admin1234 --build-arg DOMAIN_NAME=localhost:8000 --build-arg DJANGO_SETTINGS_MODULE=axioma.settings.production -t axioma:v1 . 


```