
from django.urls import path
from . import views

urlpatterns = [
    
    #endpoint for industry cards
    path('industry-cards/', views.IndustryCardListAPIView.as_view(), name='industry-card-list'),
    path('industry-cards/<int:pk>/', views.IndustryCardDetailAPIView.as_view(), name='industry-card-detail'),
    
    #endpoint for industry title
    path('industry_titles/', views.IndustryTitleListCreateAPIView.as_view(), name='industry_titles-list'),
    path('industry_titles/<int:pk>/', views.IndustryTitleDetailAPIView.as_view(), name='industry_titles-detail'),

]
