from django.urls import path
from .views import HomeHeaderCustomListCreateView,HomeHeaderCustomRetrieveUpdateDistroyView,AboutPageSectionCustomListCreateView,AboutPageSectionCustomRetrieveUpdateDistroyView,ourstoryCustomListCreateView,ourstoryCustomRetrieveUpdateDistroyView

from .views import HomeHeaderCustomListCreateView,HomeHeaderCustomRetrieveUpdateDistroyView,ServicecardCustomListCreateView,ServiceRetrieveUpdateDistroyView


urlpatterns = [
    # urls for homeheader

    path('home/headercustom/',HomeHeaderCustomListCreateView.as_view(),name="homeheadercustom-list-create"),
    path('home/headercustom/<int:pk>/',HomeHeaderCustomRetrieveUpdateDistroyView.as_view(),name="homeheadercustom-retrieve-update-distroy"),
    

    # urls for aboupagesection

    path('about_page/custom/',AboutPageSectionCustomListCreateView.as_view(),name="homeheadercustom-list-create"),
    path('about_page/custom/<int:pk>/',AboutPageSectionCustomRetrieveUpdateDistroyView.as_view(),name="homeheadercustom-retrieve-update-distroy"),

    #urls for ourstory

    path('ourstory/custom/',ourstoryCustomListCreateView.as_view(),name="homeheadercustom-list-create"),
    path('ourstory/custom/<int:pk>/',ourstoryCustomRetrieveUpdateDistroyView.as_view(),name="homeheadercustom-retrieve-update-distroy"),


    path('servicecard/custom/',ServicecardCustomListCreateView.as_view(),name="service-cards-list-create"),
    path('servicecard/custom/<int:pk>/',ServiceRetrieveUpdateDistroyView.as_view(),name="service-cards-retrieve-update-distroy"),

]