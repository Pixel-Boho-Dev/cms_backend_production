from django.urls import path
from careers import views


urlpatterns = [
    path('header/career-page/', views.CareerPageRetrieveUpdateView.as_view(), name='career-page'),
    path('career-submissions/', views.CareerSubmissionListCreateView.as_view(), name='career-submissions'),
]