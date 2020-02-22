from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('progress/', views.progress, name='progress'),
    path('api/data/', views.get_data, name='api-data'),
    path('api/chart/data/', views.ChartData.as_view()),
]