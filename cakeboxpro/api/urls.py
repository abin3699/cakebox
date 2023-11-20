from django.urls import path
from api import views

from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("cakes",views.Cakesview,basename="cakes")

urlpatterns=[
    path("register/",views.UsercreationView.as_view()),

]+router.urls