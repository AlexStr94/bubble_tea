from django.urls import path
from . import views

app_name = "bubble_tea"

urlpatterns = [
   path("screens/", views.ScreenListView.as_view(),),
   path("screens/<str:name>", views.ScreenView.as_view(),),
]
