from django.urls import path
from . import views

urlpatterns = {
    path("conclusion/", views.conclusion, name="conclusion")
}