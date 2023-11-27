from django.urls import path
from api import views

from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("cakes",views.Cakesview,basename="cakes")
router.register("carts",views.Cakesview,basename="carts")
router.register("orders",views.Orderview,basename="orders")

urlpatterns=[
    path("register/",views.UsercreationView.as_view()),

]+router.urls