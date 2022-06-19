"""blogdev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from blog.views import delete_view, index_view, create_view, update_view, detail_view, delete_view
from category.views import category_index_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', index_view, name='blog_index'),
    path('blog/create', create_view, name='blog_create'),
    path('blog/<str:pk>/update', update_view, name='blog_update'),
    path('blog/<str:pk>/', detail_view, name='blog_update'),
    path('blog/<str:pk>/delete', delete_view, name='blog_delete'),
    path('category/', category_index_view, name='category_index')
]
