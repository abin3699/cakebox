from django.urls import path
from api import views

urlpatterns=[
    path("register/",views.UsercreationView.as_view()),
]