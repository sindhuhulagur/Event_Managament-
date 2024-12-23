﻿# EVENT_MANG
# Event Management Project

## Overview

The Event Management Dashboard is a Django-based web application designed to manage events, tasks, and employee assignments. It includes role-based dashboards, task progress tracking, and secure user authentication.

---

## Features

- **Event Management**: CRUD operations for managing events.
- **Task Assignment**: Assign tasks to employees and track progress.
- **User Authentication**: Secure login, registration, and logout functionality.
- **Responsive Design**: User-friendly and mobile-compatible interface.

---

## Getting Started
# Event Management Project

## Setting Up the Virtual Environment

Follow these steps to create and activate a virtual environment for the Django project:

### Create a Virtual Environment
```bash
python -m venv venv

### Prerequisites

Make sure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)
- Virtualenv (optional but recommended)

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/event_management.git
cd event_management
2. Create and Activate a Virtual Environment
On Mac/Linux:
bash
Copy code
python3 -m venv venv
source venv/bin/activate
On Windows:
bash
Copy code
python -m venv venv
venv\Scripts\activate
3. Install Required Libraries
bash
Copy code
pip install django djangorestframework django-crispy-forms
4. Create the Django Project
bash
Copy code
django-admin startproject event_management .
5. Create the Events App
bash
Copy code
python manage.py startapp events
Database Setup
Run Migrations

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Create a Superuser

bash
Copy code
python manage.py createsuperuser
Project Structure
After setup, the project directory should look like this:

plaintext
Copy code
event_management/
├── events/               # Main app for event management
│   ├── migrations/       # Database migrations
│   ├── admin.py          # Admin configurations
│   ├── models.py         # Models for events and tasks
│   ├── views.py          # Views for handling requests
│   └── templates/        # HTML templates for the app
├── event_management/     # Django project settings
│   ├── settings.py       # Project settings
│   ├── urls.py           # Project URL configurations
├── db.sqlite3            # SQLite database
└── manage.py             # Django management script
Running the Project
Start the development server:

bash
Copy code
python manage.py runserver
Open your browser and navigate to:

arduino
Copy code
http://127.0.0.1:8000/
