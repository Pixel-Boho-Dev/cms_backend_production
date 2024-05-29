from django.urls import path
from .views import (HomeMetaRetrieveUpdateDeleteView, SocialMediaCreateView, SocialMediaRetrieveUpdateDeleteView,ServiceCreateView, ServiceListView, 
                    ServiceRetrieveUpdateDeleteView,LocationCreateView,LocationListView,LocationRetrieveUpdateDeleteView,
                    AchievementCreateView, AchievementListView, AchievementRetrieveUpdateDeleteView,HighlightCreateView, 
                    HighlightListView, HighlightRetrieveUpdateDeleteView,IndustryCreateView, IndustryListView, IndustryUpdateView,
                    MarketCreateView, MarketListView, MarketRetrieveUpdateDeleteView,HomeMetaListView,AchievementSectionListCreate,AchievementSectionRetrieveUpdateDestroy,
                    HighlightSectionListCreate,HighlightSectionRetrieveUpdateDestroy,MarketTitleCreateView,MarketTitleListView,MarketTitleRetrieveUpdateDeleteView,OurNetworkTitleCreateView,OurNetworkTitleListView,OurNetworkTitleRetrieveUpdateDeleteView

)

urlpatterns = [
    
# urls for social media create, update and delete.
    path('social-media/', SocialMediaCreateView.as_view(), name='social-media-list-create'),
    path('social-media/<int:pk>/', SocialMediaRetrieveUpdateDeleteView.as_view(), name='social-media-retrieve-update-delete'),

# urls for services.
    path('header/services/create/', ServiceCreateView.as_view(), name='service-create'),
    path('header/services/', ServiceListView.as_view(), name='service-list'),
    path('header/services/<int:pk>/', ServiceRetrieveUpdateDeleteView.as_view(), name='service-retrieve-update-delete'),

# urls for location
    path('locations/create/', LocationCreateView.as_view(), name='location-create'),
    path('locations/', LocationListView.as_view(), name='location-list'),
    path('locations/<int:pk>/', LocationRetrieveUpdateDeleteView.as_view(), name='location-retrieve-update-delete'),

# urls for ournetwork title
    path('ournetwork_title/create/', OurNetworkTitleCreateView.as_view(), name='ournetwork-title-create'),
    path('ournetwork_title/', OurNetworkTitleListView.as_view(), name='ournetwork-title-list'),
    path('ournetwork_title/<int:pk>/', OurNetworkTitleRetrieveUpdateDeleteView.as_view(), name='ournetwork-title-detail'),

# urls for achievements
    path('achievements/create/', AchievementCreateView.as_view(), name='achievement-create'),
    path('achievements/', AchievementListView.as_view(), name='achievement-list'),
    path('achievements/<int:pk>/', AchievementRetrieveUpdateDeleteView.as_view(), name='achievement-retrieve-update-delete'),

#urls for acheievement title
    path('achievementssection/',AchievementSectionListCreate.as_view(),name='achievement-section-create'),
    path('achievementssection/<int:pk>/',AchievementSectionRetrieveUpdateDestroy.as_view(),name='achievement-section-retrieve-update-delete'),

# urls for highlights
    path('highlights/create/', HighlightCreateView.as_view(), name='highlight-create'),
    path('highlights/', HighlightListView.as_view(), name='highlight-list'),
    path('highlights/<int:pk>/', HighlightRetrieveUpdateDeleteView.as_view(), name='highlight-retrieve-update-delete'),

#urls for highlight title
    path('highlightsSection/', HighlightSectionListCreate.as_view(), name='highlightsection-create'),
    path('highlightsSection/<int:pk>/', HighlightSectionRetrieveUpdateDestroy.as_view(), name='highlightsection-retrieve-update-delete'),

# Urls for industries
    path('header/industries/create/', IndustryCreateView.as_view(), name='industry-create'),
    path('header/industries/', IndustryListView.as_view(), name='industry-list'),
    path('header/industries/<int:pk>/', IndustryUpdateView.as_view(), name='IndustryUpdateView-update'),

# urls for markets header
    path('header/markets/create/', MarketCreateView.as_view(), name='market-create'),
    path('header/markets/', MarketListView.as_view(), name='market-list'),
    path('header/markets/<int:pk>/', MarketRetrieveUpdateDeleteView.as_view(), name='market-retrieve-update-delete'),

#urls for market title
    path('markets/create/',MarketTitleCreateView.as_view(),name='market-title-create'),
    path('markets/',MarketTitleListView.as_view(),name='market-title-list'),
    path('markets/<int:pk>/',MarketTitleRetrieveUpdateDeleteView.as_view(),name='market-title-retrieve-update-delete'),

# urls for meta tags in home
    path('homemeta/',HomeMetaRetrieveUpdateDeleteView.as_view(),name='home_meta_create'),
    path('homemetall/',HomeMetaListView.as_view(),name='homemeta_all')

]
