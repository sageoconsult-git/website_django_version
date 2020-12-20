from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('',views.index, name='home'),
    path('about',views.about, name='about'),
    path('blog',views.blog, name='blog'),
    path('careers',views.careers, name='careers'),
    path('contact',views.contact, name='contact'),
    path('services',views.services, name='services'),
    path('privacy',views.privacy, name='privacy'),
    path('industry',views.industry, name='industry'),
    path('test',views.test, name='test')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)