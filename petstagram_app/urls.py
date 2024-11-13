from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('petstagram_app.common.urls')),
    path('accounts/', include('petstagram_app.accounts.urls')),
    path('pets/', include('petstagram_app.pets.urls')),
    path('photos/', include('petstagram_app.photos.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)