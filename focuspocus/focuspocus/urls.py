"""
URL configuration for focuspocus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""
from django.contrib import admin
from django.urls import path, include
from tareas.views import *

from django.conf.urls.static import static 
from django.conf import settings 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Prueba.as_view()),
    path('lista/', ListarTareas.as_view(),),
    path('crear-tarea/', CrearTarea.as_view(),),
    path('actualizar-tarea/<int:pk>/', ModificarTarea.as_view(),),
    path('eliminar-tarea/<int:pk>/', EliminarTarea.as_view(),),
    path('',include('django.contrib.auth.urls')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
