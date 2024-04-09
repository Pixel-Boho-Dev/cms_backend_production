from django.urls import path
from .views import key_diffrentiatesListCreate,key_diffrentiatesRetrieveUpdateDestroy,key_diffrentiatesSectionListCreate,key_diffrentiatesSectionRetrieveUpdateDestroy

urlpatterns = [
    path('key-diffrentiates/', key_diffrentiatesListCreate.as_view(), name='key_diffrentiates-list-create'),
    path('key-diffrentiates/<int:pk>/', key_diffrentiatesRetrieveUpdateDestroy.as_view(), name='key_diffrentiates-detail'),
    path('key-diffrentiatesSection/', key_diffrentiatesSectionListCreate.as_view(), name='key_diffrentiatesSection-list-create'),
    path('key-diffrentiatesSection/<int:pk>/', key_diffrentiatesSectionRetrieveUpdateDestroy.as_view(), name='key_diffrentiatesSection-detail'),
]
