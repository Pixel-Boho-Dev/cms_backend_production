
from django.urls import path
from . import views

urlpatterns = [
    


    path('industry-cards/', views.IndustryCardListAPIView.as_view(), name='industry-card-list'),
    path('industry-cards/<int:pk>/', views.IndustryCardDetailAPIView.as_view(), name='industry-card-detail'),

    path('industry_titles/', views.IndustryTitleListCreateAPIView.as_view(), name='industry_titles-list'),
    path('industry_titles/<int:pk>/', views.IndustryTitleDetailAPIView.as_view(), name='industry_titles-detail'),

]
