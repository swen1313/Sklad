from django.urls import path
from . import views


urlpatterns = [
    path('products_list/', views.ProductListView.as_view()),
    # path("<name>/", views.index),
    path('resources/create/', views.ProductCreateView.as_view(), name='products_create'),
    path('resources/all/', views.ProductAPIListView.as_view()),
    path('resources/<int:pk>/', views.ProductAPIDetailView.as_view())
    # path("new_good/", views.new_good)
]