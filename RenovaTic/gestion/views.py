from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.contrib.auth import views
from django.shortcuts import redirect
#from django.contrib.auth.models import User

def index(request):
    #Comprobar si el usuario esta autentificado
    if request.user.is_authenticated():
        return HttpResponse("USUARIO AUTENFICIADO")
    else:
        return redirect('/login/')






# Create your views here.
