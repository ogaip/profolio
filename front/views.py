from django.shortcuts import render
from django.contrib.auth.models import User
from data.models import Profile, Project, ProgrammingLanguage,Framework, SocialNetwork, Reference, Experience
from data.forms import ContactForm

# Create your views here.

def index(request):
    titulo= "Pagina HOla"
    
    user= User.objects.filter(username="ogaip").values()
    perfil= Profile.objects.filter(user__username="ogaip").values()
    lenguajes= ProgrammingLanguage.objects.filter(user__username="ogaip").values()
    framework= Framework.objects.filter(user__username="ogaip").values()
    proyecto= Project.objects.filter(user__username="ogaip").values()
    social= SocialNetwork.objects.filter(user__username="ogaip").values()
    referencia= Reference.objects.filter(user__username="ogaip").values()
    experiencia= Experience.objects.filter(user__username="ogaip").values()
    
    
    print(experiencia)
    
    return render(request, "pages/index.html", {
        "title": titulo,
        "name": user,
        "perfil": perfil,
        "lenguajes": lenguajes,
        "framework": framework,
        "proyecto": proyecto,
        "contacto": contacto,
        "social": social,
        "experiencia": experiencia,
    })
    
def contacto(request):
    if request.method == POST:
      contact  
      