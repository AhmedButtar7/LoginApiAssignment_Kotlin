# Login API Assignment

This project is an Android application built with Kotlin, demonstrating the implementation of user authentication and a "Forgot Password" feature. It interacts with a Django REST API for backend operations.

## Features

- **User Authentication:**
  - User Signup
  - User Login
- **Forgot Password:**
  - Allows users to retrieve their password via email.
- **Django REST API Integration:**
  - Backend handles user data and email functionality.

---

## Technologies Used

### Frontend
- **Language:** Kotlin
- **UI Framework:** XML-based layouts
- **Libraries:**
  - Retrofit for HTTP requests
  - OkHttp for network logging

### Backend
- **Framework:** Django (Python)
- **Database:** SQLite (can be replaced with other relational databases)
- **Email Backend:** Outlook SMTP (via Django Email settings)
- **API Libraries:**
  - Django Rest Framework (DRF)

---

## Prerequisites

1. **Backend Requirements:**
   - Python 3.8+
   - Django 3.0+
   - Install dependencies using `pip install -r requirements.txt`.
   - Configure the `EMAIL_BACKEND` and SMTP settings in `settings.py` for email functionality.

   Example settings for Outlook:
   ```python
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.office365.com'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = '<your_outlook_email>'
   EMAIL_HOST_PASSWORD = '<your_password>'
   DEFAULT_FROM_EMAIL = '<your_outlook_email>'



Setup Instructions
Backend
Clone the repository:

bash
Copy code
git clone <repository_url>
cd <backend_directory>
Run migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Start the server:

bash
Copy code
python manage.py runserver
Ensure the backend API is reachable at http://192.168.100.102:8000/api/.

Frontend
Open the project in Android Studio.
Update the base URL in the RetrofitInstance object:
kotlin
Copy code

const val BASE_URL = "http://192.168.100.102:8000/api/"
Build and run the application on an emulator or physical device.
API Endpoints
Authentication

Signup: POST /api/users/signup/

Request Body: { "email": "example@example.com", "username": "user", "password": "password123" }
Login: POST /api/users/login/
Request Body: { "email": "example@example.com", "password": "password123" }
Forgot Password
Retrieve Password: POST /api/users/forgot/
Request Body: { "email": "example@example.com" }
Key Files
Backend

views.py: Handles API logic, including sending emails.
models.py: Defines the user schema.
urls.py: Defines API routes.
settings.py: Configures email backend and database.
Frontend

ForgotPasswordActivity.kt: Implements the "Forgot Password" feature.
LoginActivity.kt and SignupActivity.kt: Handle login and signup processes.
RetrofitInstance.kt: Configures Retrofit for API calls.

Notes
Ensure that the backend server runs on the same network as the Android device or emulator.
For production, use HTTPS instead of HTTP for secure communication.
Update SMTP credentials to match your email provider.

License
This project is licensed under the MIT License. Feel free to use and modify as needed.
