from django.urls import path
from .views import ChoosesSectionListCreateView, ChoosesSectionRetrieveUpdateDestroyView

urlpatterns = [
    
    #urls for chooses

    path('chooses/', ChoosesSectionListCreateView.as_view(), name='chooses-list-create'),
    path('chooses/<int:pk>/', ChoosesSectionRetrieveUpdateDestroyView.as_view(), name='chooses-retrieve-update-destroy'),
    
]
