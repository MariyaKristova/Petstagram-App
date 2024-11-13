from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView
from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from petstagram_app.accounts.forms import AppUserCreationForm, ProfileEditForm
from petstagram_app.accounts.models import Profile

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

class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name='accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={'pk': self.object.pk}
        )


class ProfileDetailView(DetailView):
    model = Profile
    template_name='accounts/profile-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photos_with_likes = self.object.photo_set.annotate(likes=Count('like'))
        context['total_likes_count'] = sum(p.likes for p in photos_with_likes)
        context['total_pets_count'] = self.object.pet_set.count()
        context['total_photos_count'] = self.object.photo_set.count()
        return context

def delete_profile(request, pk: int):
    return render(request, template_name='accounts/profile-delete-page.html')

