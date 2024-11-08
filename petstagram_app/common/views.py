from django.http import HttpResponse
from django.shortcuts import render, redirect, resolve_url
from django.views.generic import ListView
from pyperclip import copy

from petstagram_app.common.forms import CommentForm, SearchForm
from petstagram_app.common.models import Like
from petstagram_app.photos.models import Photo


# Create your views here.
class HomePageView(ListView):
    model = Photo
    template_name = 'common/home-page.html'
    context_object_name = 'all_photos'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['search_form'] = SearchForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        pet_name = self.request.GET.get('pet_name')

        if pet_name:
            queryset = queryset.filter(tagged_pets__name__icontains=pet_name)

        return queryset


def like_functionality(request, photo_id: int):
    photo = Photo.objects.get(id=photo_id)
    liked_object = Like.objects.filter(to_photo_id=photo_id).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=photo)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')

def share_functionality(request, photo_id: int):
    copy(request.META['HTTP_HOST'] + resolve_url('photo-details',photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')

def comment_functionality(request, photo_id):
    if request.POST:
        photo = Photo.objects.get(id=photo_id)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.to_photo = photo
            comment.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')