from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import blogPost, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy



class HomeView(ListView):
    model = blogPost
    template_name = 'blog.html'
    ordering = ['-update_date']
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu 
        return context
        
    
    
class blogDetailView(DetailView):
    model = blogPost
    template_name = 'blog-details.html' 
     
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(blogDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu 
        return context  

class AddPostView(CreateView):
    model = blogPost
    form_class = PostForm
    template_name = 'add-post.html'


def CategoryView(request, cats):
    category_post = blogPost.objects.filter(category=cats.replace('-',' '))
    return render(request, 'categorys.html', {'cats':cats, 'category_post':category_post})

class AddCategoryView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'add-category.html'


class UpdatePostView(UpdateView):
    model = blogPost
    form_class = EditForm
    template_name = 'update-post.html'
    # fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
    model = blogPost
    template_name = 'delete-post.html'
    success_url = reverse_lazy('blog')
