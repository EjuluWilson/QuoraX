"""QouraX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django_registration.backends.one_step.views import RegistrationView
from users.forms import CustomForm

urlpatterns = [
    path('admin/', admin.site.urls),

    #account reg url (custom reg view provided by django reg)
    #fo creating new accounts
    path("accounts/register",
        RegistrationView.as_View(
            form_class = CustomForm,
            success_url = "/",
        ), name= "django_registration_register"
    ),

    #urls used by the django registration pakage
    path("accounts/",
        include("django_registration.backends.one_step.urls")
    ),

    #login urls provided by django 
    path("accounts/",
        include("django.contrib.auth.urls")
    ),

    #login urls for the browserablle api 
    path("api-auth/",
        include("rest_framework.urls")
    ),

    #login endpoint to use via rest
    path("api/rest-auth/",
        include("rest_auth.urls")
    ),

    #registration enpoint to use via rest
    path("api/rest-auth/reistration/",
        include("rest_auth. registration.urls")
    ),
]
