from django.shortcuts import render

def index(request):

    return render(request, 'index.html')

def aboutme(request):

    return render(request, 'aboutme.html')

def skills(request):

    return render(request, 'skills.html')

def portafolio(request):

    return render(request, 'portafolio.html')

def contacto(request):

    return render(request, 'contacto.html')

