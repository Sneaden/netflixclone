from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("signup/",views.signup,name="signup"),
    path("signin/",views.signin,name="signin"),
    path("userlogout/",views.userlogout,name="userlogout"),
    path("payment_gateway1/",views.payment_gateway1,name="payment_gateway1"),
    path("payment_gateway2/",views.payment_gateway2,name="payment_gateway2"),
    path("mainpage/",views.mainpage,name="mainpage"),
    path("horrorlist/",views.horrorlist,name="horrorlist"),
    path("comedylist/",views.comedylist,name="comedylist"),
    path("sciencefictionlist/",views.sciencefictionlist,name="sciencefictionlist"),
    path("adultlist/",views.adultlist,name="adultlist"),
    path("thrillinglist/",views.thrillinglist,name="thrillinglist"),
    path("romancelist/",views.romancelist,name="romancelist"),
    path("searchmovie/",views.searchmovie,name="searchmovie"),
    path("wishlist/",views.wishlist,name="wishlist"),
    path("removefavourite/<int:movieid>",views.removefavourite,name="removefavourite"),
    path("addtofav/<int:movieid>",views.addtofav,name="addtofav"),
    path("video/<int:movieid>",views.video,name="video"),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('success/', views.subscription_success, name='subscription_success'),
    path('tvshows/', views.tvshows, name='tvshows'),
    path('movies/', views.movies, name='movies'),

]
