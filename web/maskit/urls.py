"""
URL configuration for maskit project.

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
from django.urls import path

# import blog.views
import performance.views

urlpatterns = [
    # path("admin/", admin.site.urls),
    # path("blog/", blog.views.index),
    # path("blog/<int:id>", blog.views.blog_detail),
    # path("write/", blog.views.create),
    path("performance/", performance.views.performance_list),
    path("performance/<int:id>", performance.views.performance_detail),
    path("alarm/", performance.views.alarm)
]
