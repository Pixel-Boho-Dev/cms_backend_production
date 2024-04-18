from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ServiceViewSet,SubServiceViewSet,ServicesMetaListView,ServicesMetaRetrieveUpdateView,SubheadingCreateView,SubheadingListView


urlpatterns = [
    # Subservices for a specific service
    path('services/<int:pk>/subservices/', ServiceViewSet.as_view({'get': 'subservices'}), name='service-subservices'),

    path('subservices/', SubServiceViewSet.as_view({'get': 'list', 'post': 'create'}), name='subservice-list-create'),

    # SubService Retrieve, Update, Delete
    path('subservices/<int:pk>/', SubServiceViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='subservice-retrieve-update-delete'),
    path('subheading/',SubheadingCreateView.as_view(),name = 'subheading-list-create'),
    path('subheading/get/',SubheadingListView.as_view(),name = 'subheading_all'),

    # meta tags for service page
    path('servicmeta/',ServicesMetaRetrieveUpdateView.as_view(),name='location_meta_data'),
    path('servicemetas/',ServicesMetaListView.as_view(),name='location_all')
]
