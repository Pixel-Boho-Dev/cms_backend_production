from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ServiceViewSet,SubServiceViewSet,ServicesMetaListView,ServiceMetaCreateView,ServicesMetaRetrieveUpdateDestroyView,SubheadingCreateView,SubheadingListView,SubheadingRetrieveUpdateDestroy,SpecializedServiceListCreate,SpecializedServiceRetrieveUpdateDestroy,SpecializedSubServiceListCreate,SpecializedSubServiceRetrieveUpdateDestroy

urlpatterns = [
    # Subservices for a specific service
    path('services/<int:pk>/subservices/', ServiceViewSet.as_view({'get': 'subservices'}), name='service-subservices'),

    path('subservices/', SubServiceViewSet.as_view({'get': 'list', 'post': 'create'}), name='subservice-list-create'),

    # SubService Retrieve, Update, Delete
    path('subservices/<int:pk>/', SubServiceViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='subservice-retrieve-update-delete'),
    
    path('subheading/',SubheadingCreateView.as_view(),name = 'subheading-list-create'),
    path('subheading/get/',SubheadingListView.as_view(),name = 'subheading_all'),
    path('subheading/<int:pk>/',SubheadingRetrieveUpdateDestroy.as_view(),name = 'subheading-retrieve-update-delete'),


    # meta tags for service page
    path('servicmeta/',ServiceMetaCreateView.as_view(),name='location_meta_data'),
    path('servicmeta/get/',ServicesMetaListView.as_view(),name='location_meta_data'),
    path('servicmeta/<int:pk>/',ServicesMetaRetrieveUpdateDestroyView.as_view(),name='location_meta_data'),
    # path('servicemetas/<int:pk>/',ServicesMetaListView.as_view(),name='location_all'),

    path('specialized-service/',SpecializedServiceListCreate.as_view(),name = 'specialized-service-list-create'),
    path('specialized-service/<int:pk>/',SpecializedServiceRetrieveUpdateDestroy.as_view(),name = 'specialized-service-retrieve-update-delete'),

     path('specialized-subservice/',SpecializedSubServiceListCreate.as_view(),name = 'specialized-subservice-list-create'),
    path('specialized-subservice/<int:pk>/',SpecializedSubServiceRetrieveUpdateDestroy.as_view(),name = 'specialized-subservice-retrieve-update-delete'),
]
