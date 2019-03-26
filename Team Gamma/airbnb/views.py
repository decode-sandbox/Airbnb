from django.shortcuts import render
import airbnb

# Create your views here.

# def index(request):
#     return render(request, airbnb/index.html, context, content_type, status, using)


def index(request):
  return render(request, 'airbnb/index.html', locals())


def login(request):
  return render(request, 'airbnb/login.html', locals())


def registration(request):
  return render(request, 'airbnb/registration.html', locals())


def contact(request):
  return render(request, 'airbnb/contact.html', locals())


def about(request):
  return render(request, 'airbnb/about.html', locals())


def hotel_homepage(request):
  return render(request, 'airbnb/hotel_homepage.html', locals())


def hotel_booking(request):
  return render(request, 'airbnb/hotel_booking.html', locals())


def holidays(request):
  return render(request, 'airbnb/holidays.html', locals())


def hotel_listing(request):
  return render(request, 'airbnb/hotel_listing.html', locals())


def travel_guide(request):
  return render(request, 'airbnb/travel_guide.html', locals())


def error_page(request):
  return render(request, 'airbnb/error_page.html', locals())


def payment_success(request):
  return render(request, 'airbnb/payment_success.html', locals())


def popup_ad(request):
  return render(request, 'airbnb/popup_ad.html', locals())


def user_profil(request):
  return render(request, 'airbnb/user_profil.html', locals())


def wishlist(request):
  return render(request, 'airbnb/wishlist.html', locals())


def cruse_search_result(request):
  return render(request, 'airbnb/cruse_search_result.html', locals())


def forgot_password(request):
  return render(request, 'airbnb/forgot_password.html', locals())
