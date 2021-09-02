from django.urls import path
from . import views


urlpatterns = [
    path("<name>/", views.index),
    # path("new_good/", views.new_good)
]