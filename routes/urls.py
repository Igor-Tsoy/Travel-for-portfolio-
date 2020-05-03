from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('find/', views.find_routes, name='find_routes'),
    path('create/', views.add_route, name='add'),
    path('list/', views.RouteListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.RouteDetailView.as_view(), name="detail"),
    path('delete/<int:pk>/', views.RouteDeleteView.as_view(), name="delete"),
]