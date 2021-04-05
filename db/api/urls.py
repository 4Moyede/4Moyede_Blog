from django.urls import path
from api import views

urlpatterns = [
    path('data', views.GetData.as_view())
]