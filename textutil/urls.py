"""textutil URL Configuration

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
from django.urls import path
from .import view
from .import visit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view.index,name='index'),
    path('fun',view.fun,name='fun'),
    path('visit', visit.had, name='visit'),
    path('punctuation',visit.punctuation,name='punctuation'),
    path('removepunc',visit.removepunc,name='removepunc'),
    path('space',visit.space,name='space'),
    path('removespace',visit.removespace,name='removespace'),
    path('charactercount',visit.charactercount,name='charactercount'),
    path('countcharacter',visit.countcharacter,name='countcharacter'),
    path('capitalize',visit.capitalize,name='capitalize'),
    path('charcapitalize',visit.charcapitalize,name='charcapitalize'),

]
