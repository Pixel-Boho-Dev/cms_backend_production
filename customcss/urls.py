from django.urls import path
from .views import HomeHeaderCustomListCreateView,HomeHeaderCustomRetrieveUpdateDistroyView,AboutPageSectionCustomListCreateView,AboutPageSectionCustomRetrieveUpdateDistroyView

urlpatterns = [
    # urls for homeheader

    path('home/headercustom/',HomeHeaderCustomListCreateView.as_view(),name="homeheadercustom-list-create"),
    path('home/headercustom/<int:pk>/',HomeHeaderCustomRetrieveUpdateDistroyView.as_view(),name="homeheadercustom-retrieve-update-distroy"),
    

    # urls for aboupagesection

    path('about_page/custom/',AboutPageSectionCustomListCreateView.as_view(),name="homeheadercustom-list-create"),
    path('about_page/custom/<int:pk>/',AboutPageSectionCustomRetrieveUpdateDistroyView.as_view(),name="homeheadercustom-retrieve-update-distroy"),


]