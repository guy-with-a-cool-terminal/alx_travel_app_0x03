# alx_travel_app_0x00

## Description

A Django-based travel listing and booking app. This version includes:

- Models: Listing, Booking, Review
- DRF serializers
- Seeder command for sample data

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Migrate and Seed

python manage.py makemigrations
python manage.py migrate
python manage.py seed

Run the App

python manage.py runserver
