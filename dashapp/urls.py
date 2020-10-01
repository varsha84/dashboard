from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('release_status/<int:release_id>/', views.release_status, name='release_status'),
    path('status_by_release_name/<release>/', views.status_by_release_name, name='status_by_release_name'),
    path('pie_json', views.piechart_json, name='piechart'),
    path('barchart_json', views.barchart_json, name ='barchart_json'),
    path('product_status', views.product_status, name ='product_status')
    
    
    
    
]