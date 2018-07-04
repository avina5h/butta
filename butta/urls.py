"""butta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
#adding include below for connecting url files of other apps
from django.urls import path, include
#to include views
from shop import views
#this is to import setting and static so that we can connect or add static images/files in the project
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index , name="index"),
    #connecting urls file of shop app
    path('shop/', include('shop.urls')),
    path('search/', include('search_app.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('account/create/', views.signupView, name='signup'),
    path('account/login/', views.signinView, name='signin'),
    path('account/logout/', views.signoutView, name='signout'),
]
#we can even add + that static(...) after the "]" above its like a settings debug style too
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)