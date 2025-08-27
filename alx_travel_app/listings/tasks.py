from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_booking_confirmation_email(user_email,booking_details):
    """
    Send a booking confirmation email to the user.
    Args:
        user_email (str): The recipient's email address
        booking_details (dict): Information about the booking
    
    Returns:
        str: Success message
    
    """
    # structure the email
    
    subject = "Booking Confirmation - ALX Travel App"
    
    message = f"""
    Dear Customer,
    
    Your booking has been confirmed! Here are the details:
    
    Booking ID: {booking_details.get('id', 'N/A')}
    Listing: {booking_details.get('listing_name', 'N/A')}
    Check-in Date: {booking_details.get('check_in', 'N/A')}
    Check-out Date: {booking_details.get('check_out', 'N/A')}
    
    Thank you for using ALX Travel App!
    
    Best regards,
    The ALX Travel Team
    """
    
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user_email],
            fail_silently=False,
        )
        
        return f"Email successfully sent to {user_email}"
    
    except Exception as e:
        print(f"Failed to send email to {user_email}: {str(e)}")
        # raise the exception again so celery knows
        raise e