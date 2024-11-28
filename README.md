# LMS Backend (Work in Progress)

This repository contains the backend code for the Learning Management System (LMS), built using Django. It provides robust APIs for managing users, courses, payments, and more.

## Features
- User Authentication (JWT)
- API Documentation with Swagger
- Student and Instructor Dashboards
- Course Management with Sections and Lessons
- Payments Integration (Stripe, PayPal)
- Notes and Q&A Management
- Review and Rating System
- Notifications System
- Coupon and Wishlist Management

## Tech Stack
- **Framework**: Django
- **Database**: PostgreSQL
- **Authentication**: Django REST Framework with JWT
- **API Documentation**: drf-yasg

## Getting Started

### Prerequisites
- Python (>= 3.8)
- PostgreSQL
- pip

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/lms-backend.git
   ```
2. Navigate to the project directory:
   ```bash
   cd lms-backend
   ```
3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Set up the database:
- Update the DATABASES setting in settings.py.
- Run migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
6. Start the development server:
    ```bash
    python manage.py runserver
    ```
