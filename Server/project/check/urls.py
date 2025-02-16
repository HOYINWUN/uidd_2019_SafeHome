"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('showdetail/', views.showDetail),
    path('engineer/showchecks/', views.engineerShowChecks),
    path('personal/showappliedcases/', views.personalShowAppliedCases),
    path('volunteer/shownotcheckedcases/', views.volunteerShowNotCheckedCases),
    path('volunteer/showcheckedcases/', views.volunteerShowCheckedCases),
    path('showunassignedcases/', views.showUnassignedCases),
    path('assign/', views.assign),
    path('result/', views.result),
    path('upload/', views.upload),
    path('', views.home),
]
