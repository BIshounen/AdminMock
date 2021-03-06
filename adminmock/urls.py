"""adminmock URL Configuration

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
from rest_framework import routers
import adminapp.views
from rest_framework.authtoken import views

admin_details = adminapp.views.AdminsViewSet.as_view({
    'patch': 'update'
})

preset_details = adminapp.views.PresetsViewSet.as_view({
    'patch': 'update'
})

router = routers.DefaultRouter()
router.register(r'api-v1-employees', adminapp.views.EmployeeViewSet)
router.register(r'api-v1-games', adminapp.views.GameViewSet)
router.register(r'api-v1-admins', adminapp.views.AdminsViewSet)
router.register(r'api-v1-game_presets', adminapp.views.PresetsViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
