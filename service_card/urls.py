# urls.py
from django.urls import path
from .views import ServicesCardListCreateView, ServicesCardRetrieveUpdateDestroyView

urlpatterns = [
    path('services_cards/', ServicesCardListCreateView.as_view(), name='services_card_list_create'),
    path('services_cards/<int:pk>/', ServicesCardRetrieveUpdateDestroyView.as_view(), name='services_card_retrieve_update_destroy'),
]
