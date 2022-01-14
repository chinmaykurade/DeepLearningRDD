from django.urls import path

from . import views

urlpatterns = [
    path('', views.stream, name='stream'),
    # path('', views.default_page, name='default_page'),
]