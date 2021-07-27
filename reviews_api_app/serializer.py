from .models import Reviews
from rest_framework import serializers


class ReviewsSerializer(serializers.ModelSerializer):

    class Meta:

        fields = ('id', 'item', 'review', 'purchaser')
        model = Reviews
