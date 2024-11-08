from django.urls import path, include

from petstagram_app.photos import views
from petstagram_app.photos.views import AddPhotoView, EditPhotoView, PhotoDetailsView

urlpatterns = [
    path('add/', AddPhotoView.as_view(), name='add-photo'),

    path('<int:pk>/', include ([
        path('', PhotoDetailsView.as_view(), name='photo-details'),
        path('edit/', EditPhotoView.as_view(), name='photo-edit'),
        path('delete/', views.photo_delete, name='photo-delete'),
         ]))
]