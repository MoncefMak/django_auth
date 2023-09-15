# Django Authentication and User Profiles

This Django project provides user authentication with JWT token-based authentication and supports three types of users: super-admin, staff, and customers. Additionally, it automatically creates user profiles upon registration.

## Features

- JWT token-based authentication
- User registration with automatic profile creation as customer
- Three user types: super-admin, stuff, and customer
- Super-admin can create Stuffs and sumer-admin users 
- API endpoints for user registration and profile management

## Installation

To set up and run this project locally, follow these steps:

1. Clone the repository:
   https://github.com/MoncefMak/django_auth.git
2. Create and activate a virtual environment (optional but recommended for isolation):
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS and Linux
   python3 -m venv venv
   source venv/bin/activate
   
4. Install the required Python packages:
  pip install -r requirements.txt
5. Run migrations:
  python manage.py makemigrations
  python manage.py migrate
4.Run the following command for creating a superUser:
  python manage.py createsuperuser
5.Add Super-Admin from Django Admin

## Running Tests

To run the project's tests, use the following command:
    python manage.py test
