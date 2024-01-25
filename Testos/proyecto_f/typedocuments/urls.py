from . import views
from django.urls import path

urlpatterns = [      
    path('', views.typedocuments, name='typedocuments'),
    path('typedocument_status_/<int:typedocument_id>/', views.change_status_typedocument, name='typedocument_status'),           
]