# Backend Intern Assignment – Notes API

This project is a Django backend application with JWT authentication and a basic frontend UI.

## Tech Stack
- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite
- HTML & JavaScript (Frontend)

## Features
- User authentication using JWT
- CRUD operations for Notes
- Role-based access
- Frontend connected with backend APIs

## Setup Instructions
1. Clone the repository
2. Install dependencies:
   pip install django djangorestframework djangorestframework-simplejwt django-cors-headers
3. Run migrations:
   python manage.py migrate
4. Create superuser:
   python manage.py createsuperuser
5. Start server:
   python manage.py runserver

## APIs
- Authentication: POST /api/token/, POST /api/token/refresh/
- Notes CRUD: GET, POST, PUT, DELETE /api/notes/

Use JWT token in Authorization header:  
Authorization: Bearer <JWT_TOKEN>

## Frontend Usage
- Open frontend/index.html in browser
- Paste JWT token
- Add title and content
- Click Save

## Scalability Notes
- Microservices architecture possible
- Redis caching possible
- Docker deployment possible
- Load balancer can handle high traffic

## Author
Sandhya Mule
