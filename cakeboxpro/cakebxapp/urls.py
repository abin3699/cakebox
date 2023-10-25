from django.urls import path
from cakebxapp.views import SignupView,SigninView,CatagoryCreateView,remove_category,\
CakecreateView,CakelistView,CakeUpdateView,remove_cakeview,CakeVarientCreateView,\
CakeDetailView,CakevariantUpdateView,remove_varient,CakeofferView,remove_offer,signout_view


urlpatterns=[
    path("register/",SignupView.as_view(),name="signup"),
    path("",SigninView.as_view(),name="signin"),
    path("catagories/add",CatagoryCreateView.as_view(),name="add-catagory"),
    path("catagories/<int:pk>/remove",remove_category,name="remove-catagory"),
    path("cakes/add",CakecreateView.as_view(),name="cake-add"),
    path("cakes/all",CakelistView.as_view(),name="cake-list"),
    path("cakes/<int:pk>/change",CakeUpdateView.as_view(),name="cake-change"),
    path("cakes/<int:pk>/remove",remove_cakeview,name="cake-remove"),
    path("cakes/<int:pk>/variants/add",CakeVarientCreateView.as_view(),name="add-variant"),
    path("cakes/<int:pk>/",CakeDetailView.as_view(),name="cake-detail"),
    path("cakes/<int:pk>/variants/change",CakevariantUpdateView.as_view(),name="update-variant"),
    path("cakes/<int:pk>,variants/remove",remove_varient,name="remove-variant"),
    path("cakes/<int:pk>/variants/offers/add",CakeofferView.as_view(),name="offer-variant"),
    path("offers/<int:pk>/remove",remove_offer,name="remove-offer"),
    path("logout/",signout_view,name="signout")



]