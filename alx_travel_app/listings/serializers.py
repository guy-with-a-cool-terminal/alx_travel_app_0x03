from .models import Listing, Booking, Review
from rest_framework import serializers

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class ListingSerializer(serializers.ModelSerializer):
    bookings = BookingSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True) 
    
    class Meta:
        model = Listing
        fields = [
            'id', 'name', 'description', 'location', 
            'price_per_night', 'available', 
            'bookings', 'reviews'
        ]