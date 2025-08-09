from django.urls import path
from django.contrib import admin
from . import views
from adminui.admin_views import AdminPreferencesView
admin.autodiscover()

urlpatterns = [
    path('ipo-subscription/', views.ipo_subscription, name='ipo_subscription'),
    path('ipo-allotment/', views.ipo_allotment, name='ipo_allotment'),
]
