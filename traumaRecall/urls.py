from django.urls import path
from . import views

urlpatterns = {
    path("traumaRecall/", views.traumaRecall, name="traumaRecall")
}