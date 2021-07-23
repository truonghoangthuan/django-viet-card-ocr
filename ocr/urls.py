from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.base, name="home"),
    path("tsv/", views.student_card_page, name="tsv"),
    path("gplx/", views.driving_license_page, name="gplx"),

    path("api/id-card/", views.IDCardAPIView.as_view(), name="api-id-card"), # This is the url use for working with IDCard api.
    path("api/student-card/", views.StudentCardAPIView.as_view(), name="api-student-card"), # This is the url use for working with StudentCard api.
    path("api/driving-license/", views.DrivingLicenseAPIView.as_view(), name="api-driving-license"), # This is the url use for working with DrivingLicense api.
]
