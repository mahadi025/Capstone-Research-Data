from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(
    "capstone",
    views.GetMethod,
)
urlpatterns = [
    path("", include(router.urls)),
]
app_name = "capstone"
