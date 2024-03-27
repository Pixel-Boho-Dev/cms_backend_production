from django.urls import path
from .views import IndustriesPageListCreateView, IndustriesPageRetrieveUpdateDeleteView,IndustriesMetaListView,IndustriesMetaRetrieveUpdateView

urlpatterns = [
    path('industries/get', IndustriesPageListCreateView.as_view(), name='industries-list-create'),
    path('industries/edit/', IndustriesPageRetrieveUpdateDeleteView.as_view(), name='industries-retrieve-update-delete'),

    path('industriesmeta/',IndustriesMetaRetrieveUpdateView.as_view(),name='industries_meta_create'),
    path('industriesmetall/',IndustriesMetaListView.as_view(),name='industriesmeta_all')
    
]