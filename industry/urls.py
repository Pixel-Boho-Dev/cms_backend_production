from django.urls import path
from .views import IndustriesPageListCreateView, IndustriesPageRetrieveUpdateDeleteView,IndustriesMetaListView,IndustriesMetaRetrieveUpdateView

urlpatterns = [
    path('industries/edit/', IndustriesPageListCreateView.as_view(), name='industries-list'),
    path('industries/edit/<int:pk>/', IndustriesPageRetrieveUpdateDeleteView.as_view(), name='industry-detail'),

    


    path('industriesmeta/',IndustriesMetaRetrieveUpdateView.as_view(),name='industries_meta_create'),
    path('industriesmetall/',IndustriesMetaListView.as_view(),name='industriesmeta_all')
    
]