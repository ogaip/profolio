from django.shortcuts import render
from .forms import ProfileForm
from .models import Profile, Project
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, "pages/index.html")

def crear(request):
    profile= ProfileForm()
    titulo= "Crea tus datos"
    
    return render(request, "pages/datos_personales/crear.html", {
        "title": titulo,
        "profile": profile,
    })
    
def listar(request):
    name = request.user
    usuario = User.objects.filter(username=name).values()
    perfil = Profile.objects.filter(user__username=name).values()
    proyectos = Project.objects.filter(user__username=name).values()
    print(usuario)
    
    titulo= "Listar tus datos"
    
    return render(request, "pages/datos_personales/listar.html", {
        "title": titulo,
        "usuario": usuario,
        "perfil": perfil,
        "proyectos": proyectos,
    })