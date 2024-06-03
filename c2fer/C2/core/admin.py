from django.contrib import admin
from .models import CustomUser, Proyecto
from .forms import RegistroUsuarioForm

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'nombre', 'is_staff', 'is_active', 'is_profesor', 'is_estudiante')
    search_fields = ('email', 'nombre')
    ordering = ('id',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Proyecto)
