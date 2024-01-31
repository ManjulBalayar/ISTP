from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('data/', views.index, name="index"),
    path('demographics/', views.get_specific_demographic_options, name="demographics"),
    path('qol-data-options/', views.get_qol_data_options, name="qol_data_options"),
    path('query-data/', views.query_data, name='query_data'),
]
