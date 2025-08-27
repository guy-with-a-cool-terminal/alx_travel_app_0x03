from django.core.management.base import BaseCommand
from listings.models import Listing

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        sample_data = [
            {
                "name": "Ocean View Apartment",
                "description": "A cozy place by the beach.",
                "location": "Miami",
                "price_per_night": 150.00,
                "available": True
            },
            {
                "name": "Mountain Cabin",
                "description": "A quiet retreat in the mountains.",
                "location": "Denver",
                "price_per_night": 100.00,
                "available": True
            },
            {
                "name": "City Loft",
                "description": "Modern apartment in the city center.",
                "location": "New York",
                "price_per_night": 200.00,
                "available": True
            }
        ]

        for listing in sample_data:
            Listing.objects.create(**listing)

        self.stdout.write(self.style.SUCCESS("Seeded database with listings"))
