from django.contrib import admin
from .models import Usuario


# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    search_fields = ('rut',)
    list_display = ("id", "rut",)
    ordering = ("id",)
    list_display_links = ("id", "rut")
