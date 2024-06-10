from django.urls import path
from .views import (OfficeCreateView, OfficeRetrieveUpdateDestroyView,OfficeListView,
                    OfficeListByLocationView,Location_pageCreateView,
                    Location_pageRetrieveUpdateDestroyView,LocationMetaListView,LocationMetaRetrieveUpdateDestroyView,Location_pageRetrieveView)

urlpatterns = [

    #urls for office

    path('offices/', OfficeCreateView.as_view(), name='office-list-create'),
    path('offices/get/',OfficeListView.as_view(),name='office-list-get'),
    path('offices/<int:pk>/', OfficeRetrieveUpdateDestroyView.as_view(), name='office-retrieve-update-destroy'),

    path('offices/by-location/<int:location_id>/', OfficeListByLocationView.as_view(), name='office-list-by-location'),
    
    #urls for header location_page

    path('header/locationpage/create/',Location_pageCreateView.as_view(),name='locationpage-create'),
    path('header/locationpage/', Location_pageRetrieveView.as_view(), name='location-list'),
    path('header/locationpage/<int:pk>/',Location_pageRetrieveUpdateDestroyView.as_view(),name='location_get_update_delete'),
    
    #urls for location meta
    
    path('locationmeta/',LocationMetaRetrieveUpdateDestroyView.as_view(),name='location_meta_data'),
    path('locationmetas/',LocationMetaListView.as_view(),name='location_all'),

]
