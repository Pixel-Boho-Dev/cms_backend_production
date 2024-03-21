from django.urls import path, include
from header.views import HeaderCreateView, HeaderRetrieveUpdateDeleteView

urlpatterns = [
    path('header/create/', HeaderCreateView.as_view(), name='header-create'),
    path('header/', HeaderRetrieveUpdateDeleteView.as_view(), name='header-retrieve-update-delete'),
    
]
