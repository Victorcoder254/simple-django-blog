from django.contrib import admin
from django.urls import path

from myapp.views import frontpage,post_detail

urlpatterns = [
    path('',frontpage, name='frontpage'),
    path('admin/', admin.site.urls),
    path('<slug:slug>/', post_detail,name='post_detail'),
]
