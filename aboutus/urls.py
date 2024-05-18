from django.urls import path
from .views import (AboutPageSectionCreateView,AboutPageSectionRetrieveView, AboutPageSectionRetrieveUpdateDestroyView,
                    OurStoryRetrieveUpdateDeleteView,OurStoryCreateView,MilestoneCreateView,
                    MilestoneRetrieveUpdateDeleteView,OurTeamCreateView,OurTeamRetrieveUpdateDeleteView,OurTeamListView,
                    WhatWeAreCreateView,WhatWeAreListView,WhatWeAreRetrieveUpdateDeleteView,CertificationRetrieveUpdateDeleteView,
                    CertificationListView,CertificationCreateView,AboutMetaListView,AboutMetaRetrieveUpdateDestroyView,CertificationTitleListCreate,
                    CertificationTitleRetrieveUpdateDestroy, OurTeamTitleCreateView,OurTeamTitleRetrieveUpdateDeleteView,OurTeamTitleListView,
                    MilestoneTitleListCreate,MilestoneTitleRetrieveUpdateDestroy,WhatWeAreTitleCreateView,WhatWeAreTitleRetrieveUpdateDeleteView,WhatWeAreTitleListView,
                    WhatWeAreTitleCreateView,WhatWeAreTitleRetrieveUpdateDeleteView,WhatWeAreTitleListView,MilestoneTitleListCreate,MilestoneTitleRetrieveUpdateDestroy)


urlpatterns = [
    
    path('header/about-page-sections/create/', AboutPageSectionCreateView.as_view(), name='about-page-section-list-create'),
    path('header/about-page-sections/', AboutPageSectionRetrieveView.as_view(), name='about-page-section-retrive'),
    path('about-page-sections/<int:pk>/', AboutPageSectionRetrieveUpdateDestroyView.as_view(), name='about-page-section-retrieve-update-destroy'),

    # urls for our story.
    
    path('our-story/create/', OurStoryCreateView.as_view(), name='our-story-create'),#not for end users
    path('our-story/', OurStoryRetrieveUpdateDeleteView.as_view(), name='our-story-update'),

    # urls for milestones
    
    path('milestones/', MilestoneCreateView.as_view(), name='milestone-create'),
    path('milestones/<int:pk>/', MilestoneRetrieveUpdateDeleteView.as_view(), name='milestone-retrieve-update-delete'),

    path('milestonetitle/', MilestoneTitleListCreate.as_view(), name='milestonetitle-create'),
    path('milestonetitle/<int:pk>/', MilestoneTitleRetrieveUpdateDestroy.as_view(),name='milestonetitle-detail'),

    # urls for our team

    path('our-team/create/', OurTeamCreateView.as_view(), name='our-team-create'),
    path('our-team/<int:pk>/', OurTeamRetrieveUpdateDeleteView.as_view(), name='our-team-detail'),
    path('our-team/', OurTeamListView.as_view(), name='our-team-list'),

    path('our-team-title/create/', OurTeamTitleCreateView.as_view(), name='our-team-title-create'),
    path('our-team-title/<int:pk>/', OurTeamTitleRetrieveUpdateDeleteView.as_view(), name='our-team-title-detail'),
    path('our-team-title/', OurTeamTitleListView.as_view(), name='our-team-title-list'),

    # urls for what we are

    path('what-we-are/create/', WhatWeAreCreateView.as_view(), name='what-we-are-create'),
    path('what-we-are/<int:pk>/', WhatWeAreRetrieveUpdateDeleteView.as_view(), name='what-we-are-detail'),
    path('what-we-are/', WhatWeAreListView.as_view(), name='what-we-are-list'),

    # urls for certifications
    
    path('certification/create/', CertificationCreateView.as_view(), name='certificate-create'),
    path('certification/<int:pk>/', CertificationRetrieveUpdateDeleteView.as_view(), name='certificate-detail'),
    path('certification/', CertificationListView.as_view(), name='certificate-list'),

    path('certificationtitle/',CertificationTitleListCreate.as_view(),name='certificate-section-create'),
    path('certificationtitle/<int:pk>/',CertificationTitleRetrieveUpdateDestroy.as_view(),name='certificate-section-retrieve-update-delete'),

    # urls for blogs meta data

    path('aboutmeta/',AboutMetaRetrieveUpdateDestroyView.as_view(),name='blog_meta_create'),
    path('aboutmetall/',AboutMetaListView.as_view(),name='blogmeta_all'),

    #urls for what we are 
    
    path('what-we-are-title/create/', WhatWeAreTitleCreateView.as_view(), name='what-we-are-title-create'),
    path('what-we-are-title/<int:pk>/', WhatWeAreTitleRetrieveUpdateDeleteView.as_view(), name='what-we-are-title-detail'),
    path('what-we-are-title/', WhatWeAreTitleListView.as_view(), name='what-we-are-title-list'),


    
]