from django.urls import path
from .views import TourCreateView, TourListView

urlpatterns = [
    path('tours/', TourCreateView.as_view(), name='create_tour'),
    path('tours_list/', TourListView.as_view(), name='tours_list'),
]
