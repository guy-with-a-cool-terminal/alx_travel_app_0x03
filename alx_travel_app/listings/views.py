from rest_framework import viewsets,status
from .models import Listing,Booking,Review
from .serializers import ListingSerializer, BookingSerializer, ReviewSerializer
from .tasks import send_booking_confirmation_email
from rest_framework.response import Response

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    def create(self,request,*args,**kwargs):
        """
        Override the create method to send a confirmation email
        after a booking is successfully created.
        
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        booking = serializer.save()
        
        booking_details = {
            'id': booking.id,
            'listing_name': booking.listing.name,
            'check_in': booking.check_in.strftime('%Y-%m-%d'),
            'check_out': booking.check_out.strftime('%Y-%m-%d'),
        }
        
        # we would do request.user to know what user to send this to
        user_email = "customer@example.com"   # this is where i would use request.user
        
        # trigger email task in the background
        task_result = send_booking_confirmation_email.delay(user_email,booking_details)
        
        # prep the response
        headers = self.get_success_headers(serializer.data)
        response_data = serializer.data
        
        response_data['email_task_id'] = task_result.id
        response_data['message'] = 'Booking created successfully. Confirmation email is being sent.'
        
        return Response(
            response_data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer