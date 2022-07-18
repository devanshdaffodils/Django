
from django.urls import path
from . import views
urlpatterns = [
    path('/mjolnir', views.home, name='home'),
]
