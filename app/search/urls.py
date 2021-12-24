
from django.urls import path
from .views import Home, search_snippet, graph, request_job


app_name='search'

urlpatterns = [
    path('', Home, name='home-page'),
    path('search/',search_snippet, name="search"),
    path('graph/<str:word>', graph, name="graph-result"),
    path('get-job/', request_job, name="get-job"),
]
