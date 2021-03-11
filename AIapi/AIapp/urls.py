from django.urls import path
from AIapp import views

urlpatterns = [
    path('',views.home,name="index"),
    path('report/',views.report,name="report"),
]