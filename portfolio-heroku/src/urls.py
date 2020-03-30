"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from .views import start_page, work_page, service_page, about_page, blog_page, contact_page


app_name = 'myProject'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', start_page, name='index'),
    path('work/', work_page, name='work'),
    path('service/', service_page, name='service'),
    path('about/', about_page, name='about'),
    path('blog/', blog_page, name='blog'),
    path('contact/', contact_page, name='contact'),
    path('book/', include('book.urls')),
    path('lol/', include('eloSearch.urls')),
    path('champion/', include('champs.urls')),
    path('items/', include('itens.urls')),
    path('chat/', include('chat.urls'))
]
