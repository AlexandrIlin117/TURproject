"""TURproject URL Configuration

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
from rest_framework.routers import DefaultRouter
from django.urls import include, path

from turapps.views import PerevalAddedViewSet, UsersViewSet, CoordsViewSet, LevelViewSet, ImageViewSet


router = DefaultRouter()
router.register('pereval', PerevalAddedViewSet)
router.register('users', UsersViewSet)
router.register('coords', CoordsViewSet)
router.register('level', LevelViewSet)
router.register('images', ImageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('api/v1/pereval_addedlist',PerevalAddedAPIList.as_view()),
    # path('api/v1/pereval_addedlist/<int:pk>/',PerevalAddedAPIList.as_view()),
]
