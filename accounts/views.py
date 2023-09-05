from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import signUpForm, EditProfilrForm
from blogs.models import Profile, blogPost


# Create your views here.


class UserRegisterView(generic.CreateView):
    form_class = signUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfilrForm
    template_name = 'registration/edit-profile.html'
    success_url = reverse_lazy('blog')
    
    def get_object(self):
        return self.request.user

# def profile(request):
#     return render(request, 'registration/profile.html')


class ShowProfileView(generic.DetailView):
    model = Profile
    template_name = 'registration/profile.html'
    
    def get_context_data(self, *args, **kwargs):
        # users = Profile.objects.all()
        context = super(ShowProfileView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context  
