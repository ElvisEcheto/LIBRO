from . import views
from django.urls import path

urlpatterns = [      
    path('', views.facilodgings, name='facilodgings'),
	path('facilodging_status_/<int:facilodging_id>/', views.change_status_facilodging, name='facilodging_status'),            
]