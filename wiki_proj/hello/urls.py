from django.urls import path

from . import views

urlpatterns=[
    path("", views.index , name = "index"),
    path("<str:name>", views.greet , name= "greet"),path("sun", views.sun , name = "sun"),path("sas", views.sas , name = "sas")   
]