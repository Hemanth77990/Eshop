
from django.http import HttpResponse
from django.template import loader
from .models import course 

# Create your views here.
def login(request):
    templates=loader.get_template('login.html')
    return HttpResponse(templates.render())

def home(request):
    z=course.objects.all().values()
    templates=loader.get_template('home.html')
    context={
        'z':z
    }
    return HttpResponse(templates.render(context,request))
