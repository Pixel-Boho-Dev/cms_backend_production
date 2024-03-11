from django.urls import path
from .views import key_diffrentiatesListCreate,key_diffrentiatesRetrieveUpdateDestroy

urlpatterns = [
    path('key-diffrentiates/', key_diffrentiatesListCreate.as_view(), name='key_diffrentiates-list-create'),
    path('key-diffrentiates/<int:pk>/', key_diffrentiatesRetrieveUpdateDestroy.as_view(), name='key_diffrentiates-detail'),
]
