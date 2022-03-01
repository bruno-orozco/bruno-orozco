from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from personal_profile import views as portafolio
from mensajes import views as formulario

urlpatterns = [
    path('', portafolio.index, name="index"),
    path('sobre-mi/', portafolio.aboutme, name="aboutme"),
    path('habilidades/', portafolio.skills, name="skills"),
    path('portafolio/', portafolio.portafolio, name="portafolio"),
    path('contacto', formulario.contacto, name="contacto"),
    path('admin/', admin.site.urls),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
