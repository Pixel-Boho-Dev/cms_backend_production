from django.urls import path
from careers import views


urlpatterns = [
    path('api/career-page/', views.CareerPageRetrieveUpdateView.as_view(), name='career-page'),
    path('api/career-submissions/', views.CareerSubmissionListCreateView.as_view(), name='career-submissions'),
]