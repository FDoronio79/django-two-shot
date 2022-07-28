from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.base import RedirectView


urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),

]