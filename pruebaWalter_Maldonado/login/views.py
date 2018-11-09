from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse

from .forms import formularioLogin
# Create your views here.
def loginPage (request):
    if request.method =='POST':
        formulario = formularioLogin(request.POST)
        if formulario.is_valid():
            usuario = request.POST['username']
            clave = request.POST['password']
            user = authenticate(username=usuario,password = clave)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('estudiante'))
                    messages.warning(request, 'Te has identificado de forma correcta')
                else:
                    messages.warning(request, 'Estudiante inactivo')
            else:
                messages.warning(request,'Estudiante y/o contrasena inactivo')
    else:
        formulario = formularioLogin()

    context = {
        'f': formulario,
    }
    return render (request, 'estudiante/login/login.html', context)

def logoutPage(request):
    logout(request)
    return HttpResponseRedirect(reverse('home_page'))