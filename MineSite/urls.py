from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Minecraftable.urls.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = 'Minecraftable.views.error_views.error_404'
handler500 = 'Minecraftable.views.error_views.error_500'
handler403 = 'Minecraftable.views.error_views.error_403'
handler400 = 'Minecraftable.views.error_views.error_400'