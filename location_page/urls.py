from django.urls import path
from .views import (OfficeListCreateView, OfficeRetrieveUpdateDestroyView,
                    OfficeListByLocationView,Location_pageCreateView,
                    Location_pageRetrieveUpdateDestroyView,LocationMetaListView,LocationMetaRetrieveUpdateDestroyView,Location_pageRetrieveView)

urlpatterns = [
    path('offices/', OfficeListCreateView.as_view(), name='office-list-create'),
    path('offices/<int:pk>/', OfficeRetrieveUpdateDestroyView.as_view(), name='office-retrieve-update-destroy'),

    path('offices/by-location/<int:location_id>/', OfficeListByLocationView.as_view(), name='office-list-by-location'),
    # views for location page datas

    path('header/locationpage/create/',Location_pageCreateView.as_view(),name='locationpage-create'),
    path('header/locationpage/', Location_pageRetrieveView.as_view(), name='location-list'),
    path('locationpage/<int:pk>',Location_pageRetrieveUpdateDestroyView.as_view(),name='location_get_update_delete'),

    path('locationmeta/',LocationMetaRetrieveUpdateDestroyView.as_view(),name='location_meta_data'),
    path('locationmetas/',LocationMetaListView.as_view(),name='location_all'),

]
