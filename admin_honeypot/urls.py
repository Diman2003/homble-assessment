from admin_honeypot import views
from django.urls import path

app_name = 'admin_honeypot'

urlpatterns = [
    path('', views.AdminHoneypot.as_view(), name='login'),
    path('index1', views.AdminHoneypot.as_view(), name='index'),
]
