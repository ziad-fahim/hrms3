from django.urls import path
from . import views


urlpatterns = [
    path("", views.positions, name="all_positions"),
    path("add/", views.create_position, name="create-position"),
]