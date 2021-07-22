from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.base, name="home"),
    path("tsv/", views.student_card_page, name="tsv"),
    path("gplx/", views.driving_license_page, name="gplx"),
    path("api/", views.IDCardAPIView.as_view(), name="api"), # This is the url use for working with api.
]
