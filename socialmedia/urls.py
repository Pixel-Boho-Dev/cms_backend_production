from django.urls import path
from .views import (HomeMetaRetrieveUpdateView, SocialMediaCreateView, SocialMediaRetrieveUpdateDeleteView,ServiceCreateView, ServiceListView, 
                    ServiceRetrieveUpdateDeleteView,LocationCreateView,LocationListView,LocationRetrieveUpdateDeleteView,
                    AchievementCreateView, AchievementListView, AchievementRetrieveUpdateDeleteView,HighlightCreateView, 
                    HighlightListView, HighlightRetrieveUpdateDeleteView,IndustryCreateView, IndustryListView, IndustryRetrieveUpdateDeleteView,
                    MarketCreateView, MarketListView, MarketRetrieveUpdateDeleteView,HomeRetrieveUpdateView,HomeListView,HomeMetaListView,Home
)

urlpatterns = [
    
# urls for social media create, update and delete.
    path('social-media/', SocialMediaCreateView.as_view(), name='social-media-list-create'),
    path('social-media/<int:pk>/', SocialMediaRetrieveUpdateDeleteView.as_view(), name='social-media-retrieve-update-delete'),

# urls for services.
    path('header/services/create/', ServiceCreateView.as_view(), name='service-create'),
    path('header/services/', ServiceListView.as_view(), name='service-list'),
    path('services/<int:pk>/', ServiceRetrieveUpdateDeleteView.as_view(), name='service-retrieve-update-delete'),

# urls for location
    path('locations/create/', LocationCreateView.as_view(), name='location-create'),
    path('locations/', LocationListView.as_view(), name='location-list'),
    path('locations/<int:pk>/', LocationRetrieveUpdateDeleteView.as_view(), name='location-retrieve-update-delete'),

# urls for achievements
    path('achievements/create/', AchievementCreateView.as_view(), name='achievement-create'),
    path('achievements/', AchievementListView.as_view(), name='achievement-list'),
    path('achievements/<int:pk>/', AchievementRetrieveUpdateDeleteView.as_view(), name='achievement-retrieve-update-delete'),

# urls for highlights

    path('highlights/create/', HighlightCreateView.as_view(), name='highlight-create'),
    path('highlights/', HighlightListView.as_view(), name='highlight-list'),
    path('highlights/<int:pk>/', HighlightRetrieveUpdateDeleteView.as_view(), name='highlight-retrieve-update-delete'),

# Urls for industries

    path('header/industries/create/', IndustryCreateView.as_view(), name='industry-create'),
    path('header/industries/', IndustryListView.as_view(), name='industry-list'),
    path('industries/<int:pk>/', IndustryRetrieveUpdateDeleteView.as_view(), name='industry-retrieve-update-delete'),

# urls for market news and all

    path('header/markets/create/', MarketCreateView.as_view(), name='market-create'),
    path('header/markets/', MarketListView.as_view(), name='market-list'),
    path('markets/<int:pk>/', MarketRetrieveUpdateDeleteView.as_view(), name='market-retrieve-update-delete'),

# urls for home details

    path('home/', HomeRetrieveUpdateView.as_view(), name='home-retrieve-update'),
    path('homeall/', HomeListView.as_view(), name='home-list'),

# urls for meta tags in home

    path('homemeta/',HomeMetaRetrieveUpdateView.as_view(),name='home_meta_create'),
    path('homemetall/',HomeMetaListView.as_view(),name='homemeta_all')

]
