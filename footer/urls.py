from django.urls import path
from .views import FooterListCreate,FooterRetrieveUpdateDestroy

urlpatterns = [
    path('footer/', FooterListCreate.as_view(), name='footer-list-create'),
    path('footer/<int:pk>/', FooterRetrieveUpdateDestroy.as_view(), name='footer-detail'),
]
