from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from core.views import paginita
from django.contrib.auth import views as auth_views
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.paginita, name='home'),
    path('ingreso_propuesta/', views.ingreso_propuesta, name='ingreso_propuesta'),
    path('redireccion/', views.redireccion, name='redireccion'),
    path('login/', views.my_login_view, name='login'),
    path('logout/', views.logout, name='logout'),
    path('projects/', views.projects, name='projects'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
