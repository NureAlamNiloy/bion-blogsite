from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import signUpForm, EditProfilrForm


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



