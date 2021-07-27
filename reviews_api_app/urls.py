from .views import ReviewsListView
from .views import ReviewsDetailsView
from django.urls import path


urlpatterns = [
    
    path('', ReviewsListView.as_view(), name='reviw_api'), 
    
    path('<int:pk>', ReviewsDetailsView.as_view(), name='detail_api'), 
    
]