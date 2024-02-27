from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('record-list/', views.recordList, name="record-list"),
    path('record-detail/<str:pk>/', views.recordDetail, name="record-detail"),
    path('record-create/', views.recordCreate, name="record-create"),
    path('record-update/<str:pk>/', views.recordUpdate, name="record-update"),
    path('record-delete/<str:pk>/', views.recordDelete, name="record-delete"),
]