from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from petstagram_app.common.forms import CommentForm
from petstagram_app.photos.forms import PhotoEditForm, PhotoAddForm
from petstagram_app.photos.models import Photo


# Create your views here.
class AddPhotoView(CreateView):
    model = Photo
    form_class = PhotoAddForm
    template_name = 'photos/photo-add-page.html'
    success_url = reverse_lazy('home')


class PhotoDetailsView(DetailView):
    model = Photo
    template_name = 'photos/photo-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm
        context['comments'] = self.object.comment_set.all()
        context['likes'] = self.object.like_set.all()
        return context


class EditPhotoView(UpdateView):
    model = Photo
    form_class = PhotoEditForm
    template_name = 'photos/photo-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('photo-details', kwargs={'pk': self.object.pk})


def photo_delete(request, pk: int):
    Photo.objects.get(pk=pk).delete()
    return redirect('home')
