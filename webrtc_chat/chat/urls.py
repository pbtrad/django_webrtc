import imp
from django.urls import URLPattern, path
from . views import main_view

urlpatterns = [
    path('', main_view, name='main_view'),
]