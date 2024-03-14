from django.urls import path
from .views import AppFooterListCreate,AppFooterRetrieveUpdateDestroy

urlpatterns = [
    path('AppFooter/', AppFooterListCreate.as_view(), name='AppFooter-list-create'),
    path('AppFooter/<int:pk>/', AppFooterRetrieveUpdateDestroy.as_view(), name='AppFooter-detail'),
]
