# urls.py
from django.urls import path
from .views import ServicesCardCreateView, ServicesCardRetrieveUpdateDestroyView,ServiceTitleListCreateView,ServiceTitleRetrieveUpdateDestroyView,servicesCardListView

urlpatterns = [

    #urls for service cards

    path('services_cards/', ServicesCardCreateView.as_view(), name='services_card_list_create'),
    path('services_cards/<int:pk>/', ServicesCardRetrieveUpdateDestroyView.as_view(), name='services_card_retrieve_update_destroy'),
    path('services_cards/', servicesCardListView.as_view(), name='services_card_list_create'),
    
    #urls for servicetitle
    
    path('service-title/', ServiceTitleListCreateView.as_view(), name='services_title_list_create'),
    path('service-title/<int:pk>/', ServiceTitleRetrieveUpdateDestroyView.as_view(), name='services_title_retrieve_update_destroy'),
]
