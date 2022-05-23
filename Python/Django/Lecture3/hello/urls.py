from django.urls import path

from . import views # the . to indicate the current directory

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("thomas", views.thomas, name="thomas"),
    path("arturo", views.arturo, name="arturo")
]
