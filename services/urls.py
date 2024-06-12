from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet,SubServiceCreateView,SubserviceListView,SubserviceRetrieveUpdateDestroy,ServicesMetaListView,ServiceMetaCreateView,ServicesMetaRetrieveUpdateDestroyView,SubheadingCreateView,SubheadingListView,SubheadingRetrieveUpdateDestroy,SpecializedServiceListCreate,SpecializedServiceRetrieveUpdateDestroy,SpecializedSubServiceListCreate,SpecializedSubServiceRetrieveUpdateDestroy

urlpatterns = [

    #url for full content of service
    path('services/<slug:slug>/subservices/', ServiceViewSet.as_view({'get': 'subservices', 'delete': 'delete_subservices'}), name='service-subservices'),
    
    #urls for subservices
    path('subservices/', SubServiceCreateView.as_view(), name='subservice-create'),
    path('subservices/get/', SubserviceListView.as_view(), name='subservice-all'),
    path('subservices/<int:pk>/', SubserviceRetrieveUpdateDestroy.as_view(), name='subservice-retrieve-update-delete'),
    
    #urls for subheading
    path('subheading/',SubheadingCreateView.as_view(),name = 'subheading-list-create'),
    path('subheading/get/',SubheadingListView.as_view(),name = 'subheading_all'),
    path('subheading/<int:pk>/',SubheadingRetrieveUpdateDestroy.as_view(),name = 'subheading-retrieve-update-delete'),

    # meta tags for service page
    path('servicemeta/',ServiceMetaCreateView.as_view(),name='location_meta_data'),
    path('servicemeta/get/',ServicesMetaListView.as_view(),name='location_meta_data'),
    path('servicemeta/<int:pk>/',ServicesMetaRetrieveUpdateDestroyView.as_view(),name='location_meta_data'),
    
    #urls for specialized service
    path('specialized-service/',SpecializedServiceListCreate.as_view(),name = 'specialized-service-list-create'),
    path('specialized-service/<int:pk>/',SpecializedServiceRetrieveUpdateDestroy.as_view(),name = 'specialized-service-retrieve-update-delete'),

    #urls for specialized subservice
    path('specialized-subservice/', SpecializedSubServiceListCreate.as_view(), name='specialized-subservice-list-create'),
    path('specialized-subservice/<slug:slug>/', SpecializedSubServiceRetrieveUpdateDestroy.as_view(), name='specialized-subservice-detail'),
]
