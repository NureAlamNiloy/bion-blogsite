from django.contrib import admin
from .models import blogPost, Category

# Register your models here.

admin.site.register(blogPost)
admin.site.register(Category)
