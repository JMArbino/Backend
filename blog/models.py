import email
from email.policy import default
from ssl import Options
from tkinter import CASCADE, image_names
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options=(
        ('draft', 'Draft'), 
        ('published', 'Published'),
        ('eliminated', 'Eliminated'),
    )
        
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=255)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    imagen = models.ImageField(upload_to='blog/photos', default='static/image.jpg')
    slug = models.SlugField(max_length=250, unique_for_date="published", null=False, unique=True)
    published = models.DateTimeField(default=timezone.now) 
    
    #El autos debería ser solo un admin
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts') 

    status = models.CharField(max_length=10, choices=options, default='draft')
    objects = models.Manager() #default manager
    postobjects = PostObjects() #Custom manager

    class Meta:
        ordering = ('-published',)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='comments')
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True) 
    
    #No sé que hace status...
    status = models.BooleanField(default=True)

    #Aquí no entiendo la diferencia entre user y profile... en teoría la FK debería apuntar al autor del comentario, un user registrado
    #user = models.ForeignKey(User, on_delete=models.PROTECT, default='', related_name='user')
    #profile = models.ForeignKey('users.Profile', on_delete=models.PROTECT, default='', related_name='profile')
    #Si dejo las lineas anteriores después no puedo acceder al sector Comments desde admnin
    

    class Meta:
        ordering = ('publish',)
    
    def __str__(self):
        return f"Comments by {self.name}"

