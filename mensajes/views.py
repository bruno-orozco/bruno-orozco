from django.shortcuts import render, redirect
from django.http.response import *
from mensajes.models import *
from django.db.models import *
from mensajes.forms import *

from django.core.mail import send_mail

from django.conf import settings

def contacto(request):

    data = {
        'form': formularioMensaje()
    }


    if request.method == 'POST':

        #subject = request.POST["nombre_contacto"]
        #message = request.POST["email"] + " " + request.POST["numero_telefono"] + "" + request.POST["mensaje"]
#
        #email_from = settings.EMAIL_HOST_USER
#
        #recipient_list = ["orozco.bruno@comunidad.uanm.mx"]
#
        #send_mail(subject, message, email_from, recipient_list) 
            
        #if form.is_valid():
        formulario = formularioMensaje(data=request.POST)
        if formulario.is_valid():



            formulario.save()
            data["mensaje"] = "Tu mensaje fue enviando correctamente. Pronto me comunicaré contigo."

        else:
            data["form"] = formulario

          
#            mensajeForm.nombre_contacto =         form.cleaned_data['nombre_contacto']
#            mensajeForm.numero_telefono =         form.cleaned_data['numero_telefono']
#            mensajeForm.email =                   form.cleaned_data['email']
#            mensajeForm.mensaje =                 form.cleaned_data['mensaje']
#
#            mensajeForm.save()

#            return redirect('index')
#
#        else:
#            form = formularioMensaje(request.GET)

    return render(request, 'contacto.html', data)