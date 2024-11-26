from django.urls import path
from . import views

urlpatterns = {
    path("installPositive/", views.installPositive, name="installPositive")
}