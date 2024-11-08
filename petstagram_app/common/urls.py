from django.urls import path
from petstagram_app.common import views
from petstagram_app.common.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('like/<int:photo_id>/', views.like_functionality, name='like'),
    path('share/<int:photo_id>/', views.share_functionality, name='share'),
    path('comment/<int:photo_id>/', views.comment_functionality, name='comment')
]