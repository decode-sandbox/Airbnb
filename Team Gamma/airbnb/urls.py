from django.conf.urls import url
from airbnb.views import index, login
from django.contrib import admin
from django.urls.conf import path
from . import views
# from Gamma.urls import urlpatterns
#
urlpatterns = [
    #url(r'^$', index, name = 'index'),
    path('index', views.index),
    path('login', views.login),
    path('registration', views.registration),
    path('contact', views.contact),
    path('about', views.about),
    path('hotel_homepage', views.hotel_homepage),
    path('hotel_booking', views.hotel_booking),
    path('holidays', views.holidays),
    path('hotel_listing', views.hotel_listing),
    path('travel_guide', views.travel_guide),
    path('error_page', views.error_page),
    path('payment_success', views.payment_success),
    path('popup_ad', views.popup_ad),
    path('user_profil', views.user_profil),
    path('wishlist', views.wishlist),
    path('cruse_search_result', views.cruse_search_result),
    path('forgot_password', views.forgot_password),
]
