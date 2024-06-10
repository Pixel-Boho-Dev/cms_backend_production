from django.urls import path
from careers import views


urlpatterns = [

    #url for header career page
    path('header/career-page/', views.CareerPageRetrieveUpdateView.as_view(), name='career-page'),

    #urls for career submissions
    path('career-submissions/', views.CareerSubmissionListCreateView.as_view(), name='career-submissions'),
    
    # urls for careersmeta
    path('careersmeta/',views.CareersMetaRetrieveUpdateDeleteView.as_view(),name='contact_meta_create'),
    path('careersmetall/',views.CareersMetaListView.as_view(),name='contactmeta_all'),
]