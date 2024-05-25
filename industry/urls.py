from django.urls import path
from .views import IndustriesPageListCreateView, IndustriesPageRetrieveUpdateDeleteView,IndustriesMetaListView,IndustriesMetaRetrieveUpdateDeleteView

urlpatterns = [
    #end point for industries block

    path('industries/edit/', IndustriesPageListCreateView.as_view(), name='industries-list'),
    path('industries/edit/<int:pk>/', IndustriesPageRetrieveUpdateDeleteView.as_view(), name='industry-detail'),
    
    #end point for industries meta

    path('industriesmeta/',IndustriesMetaRetrieveUpdateDeleteView.as_view(),name='industries_meta_create'),
    path('industriesmetall/',IndustriesMetaListView.as_view(),name='industriesmeta_all')
    
]