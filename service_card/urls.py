# urls.py
from django.urls import path
from .views import ServicesCardListCreateView, ServicesCardRetrieveUpdateDestroyView,ServiceTitleListCreateView,ServiceTitleRetrieveUpdateDestroyView

urlpatterns = [
    path('services_cards/', ServicesCardListCreateView.as_view(), name='services_card_list_create'),
    path('services_cards/<int:pk>/', ServicesCardRetrieveUpdateDestroyView.as_view(), name='services_card_retrieve_update_destroy'),
    
    path('service-title/', ServiceTitleListCreateView.as_view(), name='services_title_list_create'),
    path('service-title/<int:pk>/', ServiceTitleRetrieveUpdateDestroyView.as_view(), name='services_title_retrieve_update_destroy'),
]
