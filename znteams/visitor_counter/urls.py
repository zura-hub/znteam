

from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('visitor-count/', views.show_visitor_count, name='show_visitor_count'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)