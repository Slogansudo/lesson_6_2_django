"""
URL configuration for university project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from .views import home_page1, UserRegisterView, UsersLoginView, UsersLogoutView  # register_view, login_view,
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page1, name='home_page1'),
    path('', include('library.urls')),
    path('', include('users.urls')),
    path('register/', UserRegisterView.as_view(), name='register_view'),
    path('login/', UsersLoginView.as_view(), name='login_view'),
    path('logout/', UsersLogoutView.as_view(), name='logout')
    #path('register/users/', UserRegisterView.as_view(), name='register_u'),
    #path('login/users/', UsersLoginView.as_view(), name="login_u"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
