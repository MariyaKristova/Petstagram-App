from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from petstagram_app.common.forms import CommentForm
from petstagram_app.photos.forms import PhotoEditForm, PhotoAddForm
from petstagram_app.photos.models import Photo


# Create your views here.
class AddPhotoView(LoginRequiredMixin, CreateView):
    model = Photo
    form_class = PhotoAddForm
    template_name = 'photos/photo-add-page.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.user = self.request.user
        return super().form_valid(form)


class PhotoDetailsView(LoginRequiredMixin, DetailView):
    model = Photo
    template_name = 'photos/photo-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm
        context['comments'] = self.object.comment_set.all()
        context['likes'] = self.object.like_set.all()
        self.object.has_liked = self.object.like_set.filter(user=self.request.user).exists()
        return context


class EditPhotoView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Photo
    form_class = PhotoEditForm
    template_name = 'photos/photo-edit-page.html'

    def test_func(self):
        photo = get_object_or_404(Photo, pk=self.kwargs['pk'])
        return self.request.user == photo.user

    def get_success_url(self):
        return reverse_lazy('photo-details', kwargs={'pk': self.object.pk})



@login_required
def photo_delete(request, pk: int):
    photo = Photo.objects.get(pk=pk)
    if request.user == photo.user:
        photo.delete()
    return redirect('home')
