from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.contrib.auth import views

def index(request):
    return HttpResponse("Software de gestion de renovaciones.<br> En desarrollo.")


# Create your views here.
