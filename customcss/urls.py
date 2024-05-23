from django.urls import path
from .views import HomeHeaderCustomListCreateView,HomeHeaderCustomRetrieveUpdateDistroyView

urlpatterns = [
    path('home/headercustom/',HomeHeaderCustomListCreateView.as_view(),name="homeheadercustom-list-create"),
    path('home/headercustom/<int:pk>/',HomeHeaderCustomRetrieveUpdateDistroyView.as_view(),name="homeheadercustom-retrieve-update-distroy"),

]