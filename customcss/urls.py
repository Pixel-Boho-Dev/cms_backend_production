from django.urls import path
from .views import *

urlpatterns = [
    
    #urls for homeheader

    path('home/headercustom-css/',HomeHeaderCustomListCreateView.as_view(),name="homeheadercustom-list-create"),
    path('home/headercustom-css/<int:pk>/',HomeHeaderCustomRetrieveUpdateDistroyView.as_view(),name="homeheadercustom-retrieve-update-distroy"),

    #urls for servicecard

    path('servicecard/custom-css/',ServicecardCustomListCreateView.as_view(),name="service-cards-list-create"),
    path('servicecard/custom-css/<int:pk>/',ServiceRetrieveUpdateDistroyView.as_view(),name="service-cards-retrieve-update-distroy"),

    #urls for chooseus

    path('chooseus/custom-css/',ChooseusCustomListCreateView.as_view(),name="chooseus-custom-list-create"),
    path('chooseus/custom-css/<int:pk>/',ChooseusCustomRetrieveUpdateDistroyView.as_view(),name = 'chooseus-custom-retrieve-update-distroy'),

    #urls for ournetwork

    path('home/ournetwork/custom-css/',OurnetworkCustomListCreateView.as_view(),name="ournetwork-custom-list-create"),
    path('home/ournetwork/custom-css/<int:pk>/',OurnetworkCustomRetrieveUpdateDistroyView.as_view(),name="ournetwork-custom-retrieve-update-distroy"),

    #urls for keydiffrentiates

    path('keydiffrentiates/custom-css/',KeydiffretiatesCustomListCreateView.as_view(),name="keydiffrentiates-list-create"),
    path('keydiffrentiates/custom-css/<int:pk>/',KeydiffrentiatesCustomRetrieveUpdateDistroyView.as_view(),name="keydiffrentiates-retrieve-update-distroy"),

    #urls for Acheievments

    path('acheievement/custom-css/',AcheievmentCustomListCreateView.as_view(),name = "acheievement-list-create"),
    path('acheievement/custom-css/<int:pk>/',AcheievementCustomRetrieveUpdateDistroyView.as_view(),name="acheievement-retrieve-update-distroy"),

     #urls for Acheievments

    path('highlights/custom-css/',HighlightsCustomListCreateView.as_view(),name = "highlights-list-create"),
    path('highlights/custom-css/<int:pk>/',HighlightsCustomRetrieveUpdateDistroyView.as_view(),name="highlights-retrieve-update-distroy"),


    #urls for industriescards

    path('industries/custom-css/',IndustriesCardsCustomListCreateView.as_view(),name="industries-list-create"),
    path('industries/custom-css/<int:pk>/',IndustriesCardsCustomRetrieveUpdateDistroyView.as_view(),name="industries-retrieve-update-distroy"),

    #urls for marketupdates

    path('home/marketupdates/custom-css/',MarketUpdatesCustomListCreateView.as_view(),name="market-list-create"),
    path('home/marketupdates/custom-css/<int:pk>/',MarketUpdatesCustomRetrieveUpdateDistroyView.as_view(),name="market-retrieve-update-distroy"),

    # urls for aboupagesection

    path('about_page/custom-css/',AboutPageSectionCustomListCreateView.as_view(),name="aboupages-list-create"),
    path('about_page/custom-css/<int:pk>/',AboutPageSectionCustomRetrieveUpdateDistroyView.as_view(),name="aboutpage-retrieve-update-distroy"),

    #urls for ourstory

    path('ourstory/custom-css/',OurstoryCustomListCreateView.as_view(),name="ourstory-list-create"),
    path('ourstory/custom-css/<int:pk>/',OurstoryCustomRetrieveUpdateDistroyView.as_view(),name="ourstory-retrieve-update-distroy"),

   #urls for milestone

    path('milestone/custom-css/',MilestoneListCreateView.as_view(),name="milestones-list-create"),
    path('milestone/custom-css/<int:pk>/',MilestoneCustomRetrieveUpdateDistroyView.as_view(),name="milestone-retrieve-update-distroy"),

   #urls for ourteam

    path('ourteam/custom-css/',OurteamCustomListCreateView.as_view(),name="ourteam-list-create"),
    path('ourteam/custom-css/<int:pk>/',OurteamCustomRetrieveUpdateDistroyView.as_view(),name="ourteam-retrieve-update-distroy"),
    
    #urls for whatweare

    path('whatweare/custom-css/',WhatweareCustomListCreateView.as_view(),name="whatweare-list-create"),
    path('whatweare/custom-css/<int:pk>/',WhatweareCustomRetrieveUpdateDistroyView.as_view(),name="whatweare-retrieve-update-distroy"),


    #urls for certifications
    path('certifications/custom-css/',CertificationCustomListCreateView.as_view(),name="certifications-list-create"),
    path('certifications/custom-css/<int:pk>/',CertificationCustomRetrieveUpdateDistroyView.as_view(),name="certification-retrieve-update-distroy"),


    #urls for contactform

    path('contactform/custom-css/',ContactformCustomListCreateView.as_view(),name="contactform-list-create"),
    path('contactform/custom-css/<int:pk>/',ContactformCustomRetrieveUpdateDistroyView.as_view(),name="conatactform-retrieve-update-distroy"),

    #urls for contactform

    path('footer/custom-css/',FooterCustomCListCreateView.as_view(),name="footer-list-create"),
    path('footer/custom-css/<int:pk>/',FooterCustomRetrieveUpdateDistroyView.as_view(),name="footer-retrieve-update-distroy"),

    #urls for headeournetwork

    path('header/ournetwork/custom-css/',HeaderournetworkCustomListCreateView.as_view(),name="header-list-create"),
    path('header/ournetwork/custom-css/<int:pk>/',HeaderournetworkCustomRetrieveUpdateDistroyView.as_view(),name="headerournetwork-retrieve-update-distroy"),

    #urls for ournetworkdescription

    path('ournetwork/description/custom-css/',OurnetworkdescriptioncustomListCreateView.as_view(),name="description-list-create"),
    path('ournetwork/description/custom-css/<int:pk>/',OurnetworkdescriptionCustomRetrieveUpdateDistroyView.as_view(),name="description-retrieve-update-distroy"),

    #urls for Service

    path('service/custom-css/',ServiceCustomListCreateView.as_view(),name="description-list-create"),
    path('service/custom-css/<int:pk>/',ServiceCustomRetrieveUpdateDistroyView.as_view(),name="description-retrieve-update-distroy"),

    #urls for ournetworklocation

    path('ournetwork/location/custom-css/',OurnetworklocationcustomListCreateView.as_view(),name="location-list-create"),
    path('ournetwork/location/custom-css/<int:pk>/',OurnetworklocationCustomRetrieveUpdateDistroyView.as_view(),name="locations-retrieve-update-distroy"),
     
    #urls for ournetworkoffices

    path('ournetwork/offices/custom-css/',OurnetworkofficesCustomListCreateView.as_view(),name="office-list-create"),
    path('ournetwork/offices/custom-css/<int:pk>/',OurnetworkofficesCustomRetrieveUpdateDistroyView.as_view(),name="offices-retrieve-update-distroy"),
   
    #urls for careerspage

    path('careers/custom-css/',CareerspageCustomListCreateView.as_view(),name="careers-list-create"),
    path('careers/custom-css/<int:pk>/',CareerspageCustomRetrieveUpdateDistroyView.as_view(),name="career-retrieve-update-distroy"),
  
    #urls for headermarketsupdatecustom

    path('header/markets/custom-css/',HeadermarketupdatescustomListCreateView.as_view(),name="headermarkets-list-create"),
    path('header/markets/custom-css/<int:pk>/',HeadermarketupdatescustomRetrieveUpdateDistroyView.as_view(),name="headersmarkets-retrieve-update-distroy"),

    #urls for marketcustom

    path('markets/custom-css/',MarketCustomListCreateView.as_view(),name="markets-list-create"),
    path('markets/custom-css/<int:pk>/',MarketUpdatesCustomRetrieveUpdateDistroyView.as_view(),name="market-retrieve-update-distroy"),

    #urls for industries page

    path('header/industries/custom-css/',IndustriesHeaderCustomListCreateView.as_view(),name="industries-header-list-create"),
    path('header/industries/custom-css/<int:pk>/',IndustriesHeaderCustomRetrieveUpdateDistroyView.as_view(),name="industries-header-retrieve-update-distroy"),

    #urls for industries blocks

    path('industries/blocks/custom-css/',IndustriesBlockCustomListCreateView.as_view(),name="industries-block-list-create"),
    path('industries/block/custom-css/<int:pk>/',IndustriesBlockCustomRetrieveUpdateDistroyView.as_view(),name="industries-block-retrieve-update-distroy"),
    
    #urls for industries blocks foreign key

    path('industries/<int:pk>/custom-css/',IndustriesCustomViewSet.as_view(),name="industries-header-blocks"), 
]