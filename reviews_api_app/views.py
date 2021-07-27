from django.shortcuts import render
from .serializer import ReviewsSerializer
from django.db import models
from rest_framework import generics
from .models import Reviews
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.


class ReviewsListView(generics.ListCreateAPIView):   

    serializer_class = ReviewsSerializer
    queryset = Reviews.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)



class ReviewsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = ReviewsSerializer
    queryset = Reviews.objects.all()