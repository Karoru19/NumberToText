from django.urls import path
from . import views

urlpatterns = [path("", views.ConverterFormView.as_view(), name="converter")]
