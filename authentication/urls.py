from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
   path('', views.home , name="home"),
   path('signup', views.signup , name="signup"),
   path('signin', views.signin , name="signin"),
   path('signout', views.signout , name="signout"),
   path('activate/<uidb64>/<token>', views.activate , name="activate"),
   path('aboutus', views.aboutus , name="aboutus"),
   path('contactus', views.contactus , name="contactus"),
#plagiarismresult
]
