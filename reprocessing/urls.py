from django.urls import path
from . import views

urlpatterns = {
    path("reprocessing/", views.reprocessing, name="reprocessing")
}