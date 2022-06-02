from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('contact_form_post/',
         views.contact_form_post, name='contact_form_post'),
]
