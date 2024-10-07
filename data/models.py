from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='Profile', on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.role.name}'

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    url= models.URLField(blank=True, null=True)
    image= models.ImageField(upload_to='projects_pics/', blank=True, null=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    phone = models.CharField(max_length=20)
    message= models.CharField(max_length=500)

    def __str__(self):
        return f'Contact from {self.contact_name} - {self.contact_email} - {self.phone}'

class SocialNetwork(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.platform} - {self.username}'
    
class ProgrammingLanguage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=255, choices=[
        ('Básico', 'Básico'),
        ('Intermedio', 'Intermedio'),
        ('Avanzado', 'Avanzado')
    ])
    percentage = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} - {self.user.username}'
    
class Framework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name= models.CharField(max_length=255)
    level = models.CharField(max_length=255, choices=[
        ('Básico', 'Básico'),
        ('Intermedio', 'Intermedio'),
        ('Avanzado', 'Avanzado')
    ])
    percentage = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} - {self.user.username}'
    
    def get_absolute_url(self):
        return reverse("Framework_detail", kwargs={"pk": self.pk})


class Reference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    position = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    company = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.name
    
    
class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.company} - {self.position}'