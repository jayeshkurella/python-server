
from django.contrib import admin
from django.urls import include, path

from APIapp import views


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('api/serverinfo/', views.ServerInfoAPIView.as_view(), name='serverinfo-list'), 
    path('api/serverinfo/<int:pk>/', views.ServerInfoAPIView.as_view(), name='serverinfo-detail'),  
]

