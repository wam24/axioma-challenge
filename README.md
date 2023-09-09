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
## Desbloquear un usuario
Para desbloquear un usuario necesitamos un usuario superadmin o staff.

Para crearlo usamos el siguiente comando:
```bash
python manage.py createsuperuser
```
Debemos ingresar los datos que nos solite, ej. username, email (opcional), contraseña

Una vez tengamos el usuario iniciamos sesión, puede ser en la página de inicio al entrar a la url o en la siguiente dirección:
DOMINIO(ejemplo 127.0.0.1:8000)/admin

Una ves iniciemos sesión debemos dar clic en donde dice usuarios
<image src="https://lh3.googleusercontent.com/u/1/drive-viewer/AITFw-wKVwNrkb1cnrWfUOKwDWjxH4MPom2tusiAt9Ncv_7e-Uq8Qi_EszD7MNP0z92U79ihR33sPZ9Iv3BX3cL3WZ7QPiVZZw=w1920-h952" alt="Descripción de la imagen">

Nos cargará la siguiente página donde podremos ver la lista de nuestro usuarios registrados.
<image src="https://lh3.googleusercontent.com/fife/AKsag4N6pnB4XQ9ReNgQH-j7Yozz73QRF1VbjG908ag6_ODiSiH9tui9l5NZvECgzC2FjJIkjddbBTdyDymHRburYHxxOGgWgnddjWDCAFpu82m-tr_y5AjHbjR9YP102ggA9LwB619RnQfMrlGEi9dXzFpv2vLUVMKMdIw8v1NjVT1vS7_HXEkpYQV47PIzLctHZsnqekZGqufbH7XUJqKH9Rjqm8SWcvZknr1LxvWAsCC-J4PsJB9rvepiZoKuRLrDR8Ag2DbKsMog-0t7pJxpaEK66LUnhm7pAHubNBcIyMS-oT6DvKsYcnTOWx-XdG32pUG3vUbfQujjOd6vJEYJ-bnDGD2j3-22P6Tsa9-NKn_gqaeuQCj0PiZfZc-LqUDmUweIgdz_FItedaui2PlMv6_3rfeZ4qEVqVleEG-zTuu8U3zlhn0fYVNHBgYksPvF4QGHtjKpDcHH2eXCBYGrzOqXq15mBdm6UJn505QnkMu2CpeRa29Q2GdbFbaav6GRKffBet8F0MJdf5nmDLh7UZMTM_rJokxAHNGTd5p7DqUfPwKravdGJ314VtfOZbUw2sLc7f9Ly8EAPaVYD__ZHvsfkTDMiDXgZEC4CKp2XNSW8alWua-NNLU6pM1NDVQVeEWW6q8OfroaUait3GpmMyqsHPwfCpTfa1m5nDmUAVQ6gndJcTrUrkd8qdjQrQjB_mwRl_TvM0z-uVvoVeZrUbQNARQVRP84wYnDordsmn8lOWby_dBmtTGwL8z0vsyxOD3_AS7_Rn12-5-IYUM25ibo7hFNTW7cXQen1xSf0OkMli5dguEpnUmzjP_oCVhhJAPjVUEFYpnC_bJnR8S0pL79wcGVLaeaSI0pJmKaZExpKLgke5_Jpl-oBMGCub2noOnDrXB37R8j1cUOV48yoQMEFYi4OQ3EnSwggvoJirBnM0gcGmfTDmSCKnQFoeOFQylZ9nN2uTWxnniI7Ky1ZsLR--fT7iLgF0C0XG33wm8w1PceY1-HhRMv1Lbubm-N0kQb-eI9a-RI5ON2pS4zKTW2j0OM8ifNvO3mqSen4ptarpSKtWHRfEhz-rVzl9U0giWzBpPDwhy00Scm6elDWbi8UbMUlVyFfvPHqqC3jHYvZRwoOAj8hM6ZaGrJE6Wi3hi4lPaAqUAptlGEZIiYZaKsZkyBboci8V9V0-ewcOTErFRpi91wmEBnmLIjQLgcJ29UQbzl8edwvuD5OmfnKd0x51uu1ef5xzCWI97HDMxhN3Fpc-LTipbZK0PzyHMSPwU9Q1M-_PsChTh7EE0IXqkduR7GGYO3YldZL0p-lzBmZ_OYdIHvpHgGckBrPV_CYr1uELwAlryrHFgHqD7m2tS5kShZOGGdZJE-wxnDF5rAM6SGaGuo_BY_2Ed_aKxArlc29tAVG5IQXdhCwnvDn640EC1R5sn6L1fU_jkZKIcx8h_1DJnII3WSTxSNQuYresQMtAb2GHg15nnJpQUjScR1pzzrdpdpYot98mZmDH71E8Y1Ipib6Is7OHXfrGWJPvRvz0NOy4u_B5JxC1wmWlziGcmdn--WUOe3P49SDXWgpTyrmX2wItsI=w1920-h952" alt="Descripción de la imagen">

En el buscador colocamos el rut y le damos en el botón buscar.

Una vez filtrada lista hacemos clic en el id o rut

<image src="https://lh3.googleusercontent.com/fife/AKsag4Nqm1fU4lwH6AriaFG62H5vSrN8ady3ULtJWW0az27x94ekQO0Dzp7Sx6jPd7f79XUByfqhiu-qXQLqr8Vho2Y5YAPFeGRNb_apw2AIFCp2gZRprFV4CZpeXWGPrNxijGuHUrEl_Xp8tloMba8mJQqUuAF3xtwl0HUGAAeWeKFIO6vbiwFhQvUZ4lJtr8jJnXAWhYoSjiASFKUvedqJ-pALuHFEtyfd91--lDMFh9T83J6QRbuIN4wqIeqiWDId39Pu7AiSgqO7qN27boEqFdSB70eJN87a5fF3u1kfea94amkhC3MkiCQw5jc47_U8RuMIDRnsalGO2YmnfDm7Zajf97H9uTIH50AVHFHNGUgl0ep9nZB-X8FF91n0IqwiopT1MH4L4bDpEXI8YVnCzh-y9BjfvAxg7-fNFqmHgJ0WAULEOFPxHHLf-fDfcsj9kLj5GT51wIDPrASx7LfhjAUinzNCnZS2MCHvLFfZdkxxwVWhIXhg74l80Bio3uqpananh3srjqM5gdm1WWhLKYdbureqAxaGoz4Jv7ZvTs0lH8dK7RYCnpCIxsXfl0etbTMAGBBsmINAceK5uGMUOR2hFzs0Y32p_E9AZ9L1O70-eGiFInEijmVu-NnSsg1z-n971r_XX6Mff0I_kxsAqZH0OnXb0rL4R04Q-hyDhUn92ltK2Pm7A2yhQJ-VnuhDR_l0XremS5flCX1Wm2wlkeu3SNnqVfmgUdF3VEUjuG7LFs3JlQQnONbKdeVkWKWKHDG7WzxFZ2IuV10jR34BH5p4D6FI_4CrWiU_B4J_peibt0ekXfLC5rPA_2DaaxiLlMBGmN09iFPZo-rdQMx98n1boplThmUXuEQDD3BdsC-u0Gzq-SfPvrIHMth_MwWObwhlyMTZUfR5s1Nrff94TlNR8OlRcQ4xrN0blBVAeAzA2igi9TjxeS5KAZvpi5TvkwoR_I9qcyi3Eep3oyxJrOJtrPqo3CCstfCJl89lyw9eEyUp0Sl3o81RYLvjmW6jKV6-NGUKSQJsM63573pqM-9J6tk3q13ZPtq3Wr9aYMeCdb-_pa2qp7LQDzZwMVu-B3CxEfZnfaF-RXHtA0S9gGm4ip3Tgj8-LX8JpG8niz_BYUS8ChxSOEcHBtgDaYmGP57_rWrEWelMxcBmXpJKWyhp4IS3wInRlDeGod1yLtqw8iECrXh_brMzbtlukIaSzC1D6VsDh4H40KAqeipsLDrCW3BZ2L-1NtpTwpaKeySnpat6bOTARB6Hw2Cc8vYFdzN_Qk6_6LOdR-_CMjQpd9I5p9Udy5dMjXmu7iBbbXGhHEDZwc_0w8SOI9GK9XFLZLnkph0fItFm9g2Gq0v1Z6zUiulPR7ZZtCEb7P0SMh5ZbQL_qBIPpY4j3q6KDiigynMkxbtrx4bOPkqhXzq0pqq_nWeJ31-Gi_lz1qvvIk6zVqT3WerkjJk_hgpvdpsGvNh5wyyYHw3ycqF4R-a7QQ9eowu8YHBzmag3qHeZTmTzhIwIuicyDznFbG_kHMbXKKc6BEhCTTqFIrJEYoMQ1zmLdSf16G9MZ2n7xvaqjnESG6LaFbEkSBJv=w1920-h301" alt="Descripción de la imagen">

Nos entraremos al formulario de edición del usuario.

Buscaremos el campo estado.

<image src="https://lh3.googleusercontent.com/fife/AKsag4OeaQ6z1AzJSh0XQFjNyoRdPssvMVEqNKE8vp-TlQc-CgBxhx8yPN9eWillPZ4nTrzs5oBVfTxWKkRTL3UdzqFmmeJ0r-M5AOwMME1WICZJrP5haHDsGF7ERw1RvUSjuPeLb5J4SQGJs76WzPba3vKojuVo_WHU-N3KKN5UIOJ7KS8aTp3MbABGzhCzG2XpaNW2oML0FvBFMTiA0lQpQlD-2luPBKCn47_9Ryc_CIk7uxCIyNRT0nq4MiJFtTxX08E7MAWMjZ_18R1zG2TWkWDbSut2YdLmpLaEe2Jbe1I8tMQQhlmABZKARUrUGmDCFj3DM3oIhdPP5guwCLt5QjQ1NEUMIVasUTUWEn_fCNG9YnIh8GmViKpV5R7OH6zn1Bfc3zdpIs5l8xyzsjS0eHgFqbIoU2QjhrbLvRmxIMTilQqwaZc6rmIspj8VNzH2ppu_T8FKcOmJbiTBVvIwgytBf747SMAReI32OItAsAD-w9aiEzgD0Phvfp6OimAe1TsmYsMc9K0z8DWlH1L3o3Nkz3UvlAtGNz89YHIPKUhA7TRGA8psIlKWLm5AzZBAiwcYzMt8uiOj0wtlvEHEIrDmn2lEeAv8ZoudjJLMbrLCps0j790o0xppl3EGRsu0-K4IBn1nITKipbuaHIvhAyB1iRlJpY3FdEpWJ8Pkw5kqMWs6MUN7t9TJ5rzJP8dQXoHNTEOS-yUCHMnsJhCcpy7vINwRpsInzCZeiuox_S9Bkcm1VbJp0hq7ZfwooTPQqZoyo0YTsa7tWD-fOnmM1-qzS7Q2dVA8nE4_FOOWkf4tODCMEUrYM2SivIolLO_slIJUkT_XdAMWLfND6Q1c22BKvIqaLJiAxdT1KwBm99In5aDUN2C4q827TnLKskrJM0V0kfkiKnY-ByDfWg6_v3HtGWZpJVwTiNsqhcJu06nn3ZGCeUjzPNpkEOXEvoSO8uhcZWBArv9bJ38BqhmSo_YVKpegGrQfESu2HDrWOeGCIO7NdbU7Iun6oDd6mGdfIcFOilRe6KPcJWOL_qWiIFvK13yuoz8VFGbRzpq1xLE8RPCDG5wMQYLrPRyfsJwDQbBKvYL9rzVe0y2wYDpBheTa6DnQj6tQCiV9Pys-FGiYRr9Hf-UEkwvFdnQ1LfTnbPVUFuEpQMv48upXm9-KNKJg4shXz0BOPoRzfsLOgVRhvuTE8Oux0udtxoU2W69LISVY1GeO2K1HZy7drEcAEtJ3_vBhhY7SbKVCTsgnmLAKbniDe3b7XJbq4-9LoJSdvUcOvD93TM-FBRCCeNs4yelsqQscEMForlaXHI4cwcTpfbpS-ryPy-mIVsqXiR-sAOFQyXMrZSj_AOAjBQDPKqmevdAfkDtcS5jKxBhUU9bAVb0AOnSYVDdvspBkG_jWjlvSI0CI3fQMY8KFte9CyYz_clpgF2ouS4LO1Gq7rL8ZQKozz0q9sTApj7j4B7ZruaReRQAsloB1MBd5yKyXbnO5px8LZKcYX-D0mUTDMAdkBK5PYmInCn9A8WvIoFP_k2AqPsOBpk2GCtf2YO_AyybTPmm4gm346_JSMSavLaI2uaEJ9HDZueqg=w1920-h952" alt="Descripción de la imagen">

Cambiaremos el estado de bloqueado a activo y guardaremos los cambios.

Tambien podemos cambiar los intentos de fallidos a 0.

El usuario podrá volver a iniciar sesión.



