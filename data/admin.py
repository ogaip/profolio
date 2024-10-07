from django.contrib import admin
from .models import Profile, UserRole, Role, Project, Contact, SocialNetwork, ProgrammingLanguage, Framework, Reference, Experience
from django.contrib.auth.models import User
# Register your models here.

# TabularInline #########################################################

class SocialNetworkInlinie(admin.TabularInline):
    model= SocialNetwork
    cna_delete= False
    extra=0

class LanguageInline(admin.TabularInline):
    model= ProgrammingLanguage
    can_delete= False
    extra= 0


class ProfileInline(admin.TabularInline):
    model= Profile
    can_delete= False
    extra = 0
    
class UserRoleInline(admin.TabularInline):
    model= UserRole
    can_delete= False
    extra = 0

class ContactInline(admin.TabularInline):
    model= Contact
    can_delete= False
    extra=0
    

class ProjectInline(admin.TabularInline):
    model= Project
    can_delete= False
    extra= 0

class SocialNetworkInline(admin.TabularInline):
    model= SocialNetwork
    can_delete=False
    extra=0
    
class FrameworkInline(admin.TabularInline):
    model= Framework
    can_delete=False
    extra=0
    
# mostrar en admin ############################################################

class ProfileAdmin(admin.ModelAdmin):
    inlines = [ProfileInline, UserRoleInline, ProjectInline, ContactInline, SocialNetworkInline, LanguageInline, FrameworkInline, SocialNetworkInline]
    class Meta:
        model= Profile

class RoleAdmin(admin.ModelAdmin):
    class Meta:
        model= Role
    
class UserRoleAdmin(admin.ModelAdmin):
    inline= [UserRoleInline]
    class Meta:
        model= UserRole

class ProjectAdmin(admin.ModelAdmin):
    inline= []
    class Meta:
        model = Project
    

class ContactAdmin(admin.ModelAdmin):
    class Meta:
        model = Contact

class LanguaProgrammingAdmin(admin.ModelAdmin):
    class Meta:
        model= ProgrammingLanguage
        
class FrameworkAdmin(admin.ModelAdmin):
    class Meta:
        model= Framework

class ReferenceAdmin(admin.ModelAdmin):
    class Meta:
        model= Reference
        
class ExperienceAdmin(admin.ModelAdmin):
    class Meta:
        model= Experience
    
admin.site.unregister(User)
admin.site.register(Profile)
admin.site.register(Role)
admin.site.register(UserRole)
admin.site.register(Project)
admin.site.register(Contact)
admin.site.register(SocialNetwork)
admin.site.register(ProgrammingLanguage)
admin.site.register(Framework)  
admin.site.register(Reference)
admin.site.register(Experience)
admin.site.register(User, ProfileAdmin)
