from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.contrib.auth import views
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.template.response import TemplateResponse
#from django.contrib.auth.models import User

def index(request):
    #Comprobar si el usuario esta autentificado
    if request.user.is_authenticated():
        texto = HttpResponse("USUARIO AUTENFICIADO: [<b>"+ request.user.username + "</b>] <a href='./end_session/'>SALIR</a>" )
        #return texto
        return  TemplateResponse (request, 'RenovaTic/dashboard.html')

    else:
        return redirect('/login/')

def end_session(request):
    logout(request)
    return redirect('/login/')





# Create your views here.
