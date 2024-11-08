from django.urls import path, include
from petstagram_app.accounts import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/<int:pk>', include([
        path('', views.show_profile_details, name='profile-details'),
        path('edit/', views.profile_edit, name='profile-edit'),
        path('delete', views.delete_profile, name='profile-delete'),
    ]))
]