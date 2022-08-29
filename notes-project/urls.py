"""notes-project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth.views import LoginView
from django.urls import path, include, re_path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from users.views import AuthorCreationView

react_reroute_pattern = r'^(?!(api|admin|signup)).*$'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/notes/', include('notes.urls')),
    path('api/users/', include('users.urls')),
    path('signup/', AuthorCreationView.as_view(), name='signup'),
    path('', LoginView.as_view(template_name = 'login.html'), name='login'),
    re_path(react_reroute_pattern, login_required(TemplateView.as_view(template_name="index.html"), login_url='/')),
]
