# EVENT_MANG
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

# Event Management Project

## Setting Up the Virtual Environment

Follow these steps to create and activate a virtual environment for the Django project:

### Create a Virtual Environment

# Event Management Project

## Setting Up the Virtual Environment

Follow these steps to create and activate a virtual environment for the Django project:

### Create a Virtual Environment

```bash
python -m venv venv

Activate the Virtual Environment
On Mac/Linux:
bash
Copy code
source venv/bin/activate
On Windows:
bash
Copy code
venv\Scripts\activate
Prerequisites
Make sure you have the following installed:

Python 3.8 or higher
pip (Python package manager)
Virtualenv (optional but recommended)
Installation
1. Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/event_management.git
cd event_management
2. Install Required Libraries
bash
Copy code
pip install django djangorestframework django-crispy-forms
3. Create the Django Project
bash
Copy code
django-admin startproject event_management .
4. Create the Events App
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
