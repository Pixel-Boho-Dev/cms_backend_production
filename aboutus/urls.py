from django.urls import path
from .views import (AboutPageSectionListCreateView, AboutPageSectionRetrieveUpdateDestroyView,
                    OurStoryRetrieveUpdateDeleteView,OurStoryCreateView,MilestoneCreateView,
                    MilestoneRetrieveUpdateDeleteView,OurTeamCreateView,OurTeamRetrieveUpdateDeleteView,OurTeamListView,
                    WhatWeAreCreateView,WhatWeAreListView,WhatWeAreRetrieveUpdateDeleteView,CertificationRetrieveUpdateDeleteView,
                    CertificatioListView,CertificationCreateView,AboutMetaListView,AboutMetaRetrieveUpdateView)

urlpatterns = [
    path('header/about-page-sections/', AboutPageSectionListCreateView.as_view(), name='about-page-section-list-create'),
    path('about-page-sections/<int:pk>/', AboutPageSectionRetrieveUpdateDestroyView.as_view(), name='about-page-section-retrieve-update-destroy'),

    # urls for our story.
   
    path('our-story/create/', OurStoryCreateView.as_view(), name='our-story-create'),#not for end users
    path('our-story/', OurStoryRetrieveUpdateDeleteView.as_view(), name='our-story-update'),

    # urls for milestones
    path('milestones/', MilestoneCreateView.as_view(), name='milestone-create'),
    path('milestones/<int:pk>/', MilestoneRetrieveUpdateDeleteView.as_view(), name='milestone-retrieve-update-delete'),

    # urls for our team

    path('our-team/create/', OurTeamCreateView.as_view(), name='our-team-create'),
    path('our-team/<int:pk>/', OurTeamRetrieveUpdateDeleteView.as_view(), name='our-team-detail'),
    path('our-team/', OurTeamListView.as_view(), name='our-team-list'),

    # urls for what we are

    path('what-we-are/create/', WhatWeAreCreateView.as_view(), name='what-we-are-create'),
    path('what-we-are/<int:pk>/', WhatWeAreRetrieveUpdateDeleteView.as_view(), name='what-we-are-detail'),
    path('what-we-are/', WhatWeAreListView.as_view(), name='what-we-are-list'),

    # urls for certifications
    path('certification/create/', CertificationCreateView.as_view(), name='what-we-are-create'),
    path('certification/<int:pk>/', CertificationRetrieveUpdateDeleteView.as_view(), name='what-we-are-detail'),
    path('certification/', CertificatioListView.as_view(), name='what-we-are-list'),

    # urls for blogs meta data

    path('aboutmeta/',AboutMetaRetrieveUpdateView.as_view(),name='blog_meta_create'),
    path('aboutmetall/',AboutMetaListView.as_view(),name='blogmeta_all')
    
]
