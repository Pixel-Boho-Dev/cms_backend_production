from django.urls import path
from .views import *

urlpatterns = [
    # urls for homeheader

    path('home/headercustom/',HomeHeaderCustomListCreateView.as_view(),name="homeheadercustom-list-create"),
    path('home/headercustom/<int:pk>/',HomeHeaderCustomRetrieveUpdateDistroyView.as_view(),name="homeheadercustom-retrieve-update-distroy"),

    #urls for servicecard

    path('servicecard/custom/',ServicecardCustomListCreateView.as_view(),name="service-cards-list-create"),
    path('servicecard/custom/<int:pk>/',ServiceRetrieveUpdateDistroyView.as_view(),name="service-cards-retrieve-update-distroy"),

    #urls for chooseus

    path('chooseus/custom/',ChooseusCustomListCreateView.as_view(),name="chooseus-custom-list-create"),
    path('chooseus/custom/<int:pk>/',ChooseusCustomRetrieveUpdateDistroyView.as_view(),name = 'chooseus-custom-retrieve-update-distroy'),

    #urls for ournetwork

    path('ournetwork/custom/',OurnetworkCustomListCreateView.as_view(),name="ournetwork-custom-list-create"),
    path('ournetwork/custom/<int:pk>/',OurnetworkCustomRetrieveUpdateDistroyView.as_view(),name="ournetwork-custom-retrieve-update-distroy"),
    
    # urls for aboupagesection

    path('about_page/custom/',AboutPageSectionCustomListCreateView.as_view(),name="homeheadercustom-list-create"),
    path('about_page/custom/<int:pk>/',AboutPageSectionCustomRetrieveUpdateDistroyView.as_view(),name="homeheadercustom-retrieve-update-distroy"),

    #urls for ourstory

    path('ourstory/custom/',ourstoryCustomListCreateView.as_view(),name="homeheadercustom-list-create"),
    path('ourstory/custom/<int:pk>/',ourstoryCustomRetrieveUpdateDistroyView.as_view(),name="homeheadercustom-retrieve-update-distroy"),

   #urls for milestone

    path('milestone/custom/',milestoneListCreateView.as_view(),name="service-cards-list-create"),
    path('milestone/custom/<int:pk>/',milestoneCustomRetrieveUpdateDistroyView.as_view(),name="milestone-retrieve-update-distroy"),

   #urls for ourteam

    path('ourteam/custom/',ourteamCustomListCreateView.as_view(),name="service-cards-list-create"),
    path('ourteam/custom/<int:pk>/',ourteamCustomRetrieveUpdateDistroyView.as_view(),name="ourteam-retrieve-update-distroy"),
    
    #urls for whatweare
    path('whatweare/custom/',whatweareCustomListCreateView.as_view(),name="service-cards-list-create"),
    path('whatweare/custom/<int:pk>/',whatweareCustomRetrieveUpdateDistroyView.as_view(),name="whatweare-retrieve-update-distroy"),

    #urls for contactform
    path('contactform/custom/',contactformCustomListCreateView.as_view(),name="service-cards-list-create"),
    path('contactform/custom/<int:pk>/',contactformCustomRetrieveUpdateDistroyView.as_view(),name="conatactform-retrieve-update-distroy"),

    #urls for footer
        #urls for contactform
    path('footer/custom/',footerCustomCListCreateView.as_view(),name="service-cards-list-create"),
    path('footer/custom/<int:pk>/',footerCustomRetrieveUpdateDistroyView.as_view(),name="footer-retrieve-update-distroy"),

    













  
]