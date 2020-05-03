from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('create/', views.TrainCreateView.as_view(), name='add'),
    path('update/<int:pk>/', views.TrainUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.TrainDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', views.TrainDetailView.as_view(), name="detail_view"),

]
