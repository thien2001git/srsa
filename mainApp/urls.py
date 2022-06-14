from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('danh-sach-chia', views.danhSachChia, name='danh-sach-chia'),
]