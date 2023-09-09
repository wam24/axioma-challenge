from .base import *
DEBUG = False
from os import environ

ALLOWED_HOSTS = environ.get('DJANGO_ALLOWED_HOSTS', '*').split(r'\s*,\s*')
