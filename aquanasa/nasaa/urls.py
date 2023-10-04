from django.urls import path
from . import views
from .views import HomePageView, SearchResultsView


urlpatterns = [
    path('', views.home, name='login'),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path("home/", views.index, name="home"),
]