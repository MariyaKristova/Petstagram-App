from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

UserModel = get_user_model()

class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = UserCreationForm
    template_name= 'accounts/register-page.html'
    success_url = reverse_lazy('login')

def login(request):
    return render(request, template_name='accounts/login-page.html')

def show_profile_details(request, pk: int):
    return render(request, template_name='accounts/profile-details-page.html')

def profile_edit(request, pk: int):
    return render(request, template_name='accounts/profile-edit-page.html')

def delete_profile(request, pk: int):
    return render(request, template_name='accounts/profile-delete-page.html')

