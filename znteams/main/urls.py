

from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.index, name='home'),
    path('service', views.service, name='service'),
    path('contact', views.contact, name='contact'),
    path('projects/', views.display_items, name='display_items'),
    path('about', views.about, name='about'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)