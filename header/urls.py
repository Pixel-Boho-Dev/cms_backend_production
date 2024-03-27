from django.urls import path, include
from header.views import HeaderCreateView, HeaderRetrieveUpdateDeleteView

urlpatterns = [
    path('home/header/create/', HeaderCreateView.as_view(), name='header-create'),
    path('home/header/', HeaderRetrieveUpdateDeleteView.as_view(), name='header-retrieve-update-delete'),
    
]
