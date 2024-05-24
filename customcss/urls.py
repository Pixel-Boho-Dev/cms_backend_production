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

    path('acheievement/custom/',AcheievmentCustomListCreateView.as_view(),name = "acheievement-list-create"),
    path('acheievement/custom/<int:pk>/',AcheievementCustomRetrieveUpdateDistroyView.as_view(),name="acheievement-retrieve-update-distroy"),

     #urls for Acheievments

    path('highlights/custom/',HighlightsCustomListCreateView.as_view(),name = "highlights-list-create"),
    path('highlights/custom/<int:pk>/',HighlightsCustomRetrieveUpdateDistroyView.as_view(),name="highlights-retrieve-update-distroy"),


    #urls for industriescards

    path('industries/custom-css/',IndustriesCardsCustomListCreateView.as_view(),name="industries-list-create"),
    path('industries/custom-css/<int:pk>/',IndustriesCardsCustomRetrieveUpdateDistroyView.as_view(),name="industries-retrieve-update-distroy"),

    #urls for marketupdates

    path('marketupdates/custom-css/',MarketUpdatesCustomListCreateView.as_view(),name="market-list-create"),
    path('marketupdates/custom-css/<int:pk>/',MarketUpdatesCustomRetrieveUpdateDistroyView.as_view(),name="market-retrieve-update-distroy"),

    # urls for aboupagesection

    path('about_page/custom-css/',AboutPageSectionCustomListCreateView.as_view(),name="aboupages-list-create"),
    path('about_page/custom-css/<int:pk>/',AboutPageSectionCustomRetrieveUpdateDistroyView.as_view(),name="aboutpage-retrieve-update-distroy"),

    #urls for ourstory

    path('ourstory/custom-css/',ourstoryCustomListCreateView.as_view(),name="ourstory-list-create"),
    path('ourstory/custom-css/<int:pk>/',ourstoryCustomRetrieveUpdateDistroyView.as_view(),name="ourstory-retrieve-update-distroy"),

   #urls for milestone

    path('milestone/custom-css/',milestoneListCreateView.as_view(),name="milestones-list-create"),
    path('milestone/custom-css/<int:pk>/',milestoneCustomRetrieveUpdateDistroyView.as_view(),name="milestone-retrieve-update-distroy"),

   #urls for ourteam

    path('ourteam/custom-css/',ourteamCustomListCreateView.as_view(),name="ourteam-list-create"),
    path('ourteam/custom-css/<int:pk>/',ourteamCustomRetrieveUpdateDistroyView.as_view(),name="ourteam-retrieve-update-distroy"),
    
    #urls for whatweare
    path('whatweare/custom-css/',whatweareCustomListCreateView.as_view(),name="whatweare-list-create"),
    path('whatweare/custom-css/<int:pk>/',whatweareCustomRetrieveUpdateDistroyView.as_view(),name="whatweare-retrieve-update-distroy"),

    #urls for contactform
    path('contactform/custom-css/',contactformCustomListCreateView.as_view(),name="contactform-list-create"),
    path('contactform/custom-css/<int:pk>/',contactformCustomRetrieveUpdateDistroyView.as_view(),name="conatactform-retrieve-update-distroy"),

    #urls for contactform
    path('footer/custom-css/',footerCustomCListCreateView.as_view(),name="footer-list-create"),
    path('footer/custom-css/<int:pk>/',footerCustomRetrieveUpdateDistroyView.as_view(),name="footer-retrieve-update-distroy"),

    #urls for headeournetwork
    path('header/ournetwork/custom-css/',headerournetworkCustomListCreateView.as_view(),name="header-list-create"),
    path('header/ournetwork/custom-css/<int:pk>/',headerournetworkCustomRetrieveUpdateDistroyView.as_view(),name="headerournetwork-retrieve-update-distroy"),

    #urls for ournetworkdescription
    path('ournetwork/description/custom-css/',ournetworkdescriptioncustomListCreateView.as_view(),name="description-list-create"),
    path('ournetwork/description/custom-css/<int:pk>/',ournetworkdescriptionCustomRetrieveUpdateDistroyView.as_view(),name="description-retrieve-update-distroy"),

    #urls for Service
    path('service/custom-css/',ServiceCustomListCreateView.as_view(),name="description-list-create"),
    path('service/custom-css/<int:pk>/',ServiceCustomRetrieveUpdateDistroyView.as_view(),name="description-retrieve-update-distroy"),

    #urls for ournetworklocation
    path('ournetwork/location/custom-css/',ournetworklocationcustomListCreateView.as_view(),name="location-list-create"),
    path('ournetwork/location/custom-css/<int:pk>/',ournetworklocationCustomRetrieveUpdateDistroyView.as_view(),name="locations-retrieve-update-distroy"),
     
    #urls for ournetworkoffices
    path('ournetwork/offices/custom-css/',ournetworkofficesCustomListCreateView.as_view(),name="office-list-create"),
    path('ournetwork/offices/custom-css/<int:pk>/',ournetworkofficesCustomRetrieveUpdateDistroyView.as_view(),name="offices-retrieve-update-distroy"),
   
    #urls for careerspage
    path('careers/custom-css/',careerspageCustomListCreateView.as_view(),name="careers-list-create"),
    path('careers/custom-css/<int:pk>/',careerspageCustomRetrieveUpdateDistroyView.as_view(),name="career-retrieve-update-distroy"),

    #urls for industries page
    path('header/industries/custom-css/',IndustriesHeaderCustomListCreateView.as_view(),name="industries-header-list-create"),
    path('header/industries/custom-css/<int:pk>/',IndustriesHeaderCustomRetrieveUpdateDistroyView.as_view(),name="industries-header-retrieve-update-distroy"),

  
]