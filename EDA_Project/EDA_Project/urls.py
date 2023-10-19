"""monthly_project1 URL Configuration

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
from Cct_anal.views import index, participant, data_disc1, data_disc2, data_disc3, data_anal1, data_anal2, data_anal3, data_anal4, data_anal5
urlpatterns = [
    path("",index),
    path("participants/",participant),
    path("data_disc/purpose",data_disc1),
    path("data_disc/columns",data_disc2),
    path("data_disc/hypothesis",data_disc3),
    path("data_anal/theory1",data_anal1),
    path("data_anal/theory2",data_anal2),
    path("data_anal/theory3",data_anal3),
    path("data_anal/theory4",data_anal4),
    path("data_anal/Graph",data_anal5),
    path('admin/', admin.site.urls),
]
