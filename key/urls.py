from django.urls import path
from .views import key_diffrentiatesListCreate,key_diffrentiatesRetrieveUpdateDestroy,key_diffrentiatesSectionListCreate,key_diffrentiatesSectionRetrieveUpdateDestroy

urlpatterns = [

    #urls for keydiffrentiates

    path('key-diffrentiates/', key_diffrentiatesListCreate.as_view(), name='key_diffrentiates-list-create'),
    path('key-diffrentiates/<int:pk>/', key_diffrentiatesRetrieveUpdateDestroy.as_view(), name='key_diffrentiates-detail'),
    
    #urls for keydiffrentiates title
    
    path('key-diffrentiatestitle/', key_diffrentiatesSectionListCreate.as_view(), name='key_diffrentiatestitle-list-create'),
    path('key-diffrentiatestitle/<int:pk>/', key_diffrentiatesSectionRetrieveUpdateDestroy.as_view(), name='key_diffrentiatestitle-detail'),
]
