from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from petstagram_app.accounts.forms import AppUserCreationForm

UserModel = get_user_model()

class AppUserLoginView(LoginView):
    template_name = 'accounts/login-page.html'

class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)

        return response

def show_profile_details(request, pk: int):
    return render(request, template_name='accounts/profile-details-page.html')

def profile_edit(request, pk: int):
    return render(request, template_name='accounts/profile-edit-page.html')

def delete_profile(request, pk: int):
    return render(request, template_name='accounts/profile-delete-page.html')

