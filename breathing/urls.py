from django.urls import path
from . import views

urlpatterns = {
    path("breathing/", views.breathing, name="breathing")
}