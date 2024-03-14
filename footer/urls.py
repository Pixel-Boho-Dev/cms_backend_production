from django.urls import path
from .views import FooterListCreate,FooterRetrieveUpdateDestroy

urlpatterns = [
    path('Footer/', FooterListCreate.as_view(), name='footer-list-create'),
    path('Footer/<int:pk>/', FooterRetrieveUpdateDestroy.as_view(), name='footer-detail'),
]
