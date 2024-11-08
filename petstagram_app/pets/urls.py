from django.urls import path, include
from petstagram_app.pets.views import EditPetView, DeletePetView, AddPetView, PetDetailsView

urlpatterns = [
    path('add/', AddPetView.as_view(), name='add-pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
    path('', PetDetailsView.as_view(), name='pet-details'),
    path('edit/', EditPetView.as_view(), name='pet-edit'),
    path('delete/', DeletePetView.as_view(), name='pet-delete'),
    ]))
]