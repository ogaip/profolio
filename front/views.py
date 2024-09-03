from django.shortcuts import render
from django.contrib.auth.models import User
from data.models import Profile, Project, ProgrammingLanguage,Framework
from data.forms import ContactForm

# Create your views here.

def index(request):
    titulo= "Pagina HOla"
    
    user= User.objects.filter(username="ogaip")
    perfil= Profile.objects.filter(user__username="ogaip").values()
    lenguajes= ProgrammingLanguage.objects.filter(user__username="ogaip").values()
    framework= Framework.objects.filter(user__username="ogaip").values()
    proyecto= Project.objects.filter(user__username="ogaip").values()
    contacto= ContactForm()
    
    print(contacto)
    
    return render(request, "pages/index.html", {
        "title": titulo,
        "name": user,
        "perfil": perfil,
        "lenguajes": lenguajes,
        "framework": framework,
        "proyecto": proyecto,
        "contacto": contacto,
    })
    
def contacto(request):
    if request.method == POST:
      contact  
      