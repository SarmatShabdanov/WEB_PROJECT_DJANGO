from django.urls import path
from. import views

urlpatterns = [
    path('collec/', views.коллекция_add, name='коллекция_add'),
    path('provider/', views.поставщик_add, name='поставщик_add'),  
    path('accounting/', views.бух_учет_add, name='бух_учет_add'), 
    path('catalog/', views.каталог_add, name='каталог_add'), 
    
    
]
