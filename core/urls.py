from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('detail/<int:pk>/', views.CityDetailView.as_view(), name="detail_view"),
    path('add/', views.CityCreateView.as_view(), name='add'),
    path('update/<int:pk>/', views.CityUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.CityDeleteView.as_view(), name='delete'),


]