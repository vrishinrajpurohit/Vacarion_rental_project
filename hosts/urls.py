from django.contrib import admin
from django.urls import path
from .views import Signupview,ProfileView,HostListings,ProfileUpdateView,ProfileDeleteView
from django.contrib.auth.views import LoginView
from .forms import EmailOrUsernameAuthenticationForm

urlpatterns = [
    path('login/',LoginView.as_view(authentication_form=EmailOrUsernameAuthenticationForm),name='login'),
    path('signup/', Signupview.as_view(),name="signup"),
    path('profile/', ProfileView.as_view(),name="hosthome"),
    path('profile/update', ProfileUpdateView.as_view(),name="profileupdate"),
    path('profile/delete', ProfileDeleteView.as_view(),name="profiledelete"),
    path('listings/', HostListings.as_view(),name="my_listings"),

]
