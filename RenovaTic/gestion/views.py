from django.http import HttpResponse

def index(request):
    return HttpResponse("Software de gestion de renovaciones.<br> En desarrollo.")

# Create your views here.
