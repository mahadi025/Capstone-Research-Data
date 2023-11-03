from django.urls import path
from . import views


urlpatterns = [
    path("", views.getRoutes, name="routes"),
    path("capstone-data/", views.getList, name="capstone-data-list"),
    path("capstone-data/<str:pk>/", views.getData, name="capstone-data"),
]
