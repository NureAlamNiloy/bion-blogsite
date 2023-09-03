from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=140)
    
    def __str__(self):
        return self.category_name
    
    def get_absolute_url(self):
        return reverse('blog')

class blogPost(models.Model):
    title = models.CharField(max_length=478)
    title_tag = models.CharField(max_length=200, default="Niloy-Blogs")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=100, default="phitron")
    image = models.ImageField(null = True, blank= True, upload_to = 'photos/blog')
    
    def __str__(self):
        return f"{self.title} => {self.author}" 
    
    def get_absolute_url(self):
        return reverse('blog')
    