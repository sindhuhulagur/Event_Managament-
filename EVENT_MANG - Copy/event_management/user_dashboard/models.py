from django.db import models
from django.contrib.auth.models import User

# Event Model
class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who created the event
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateField()
    category = models.CharField(max_length=50)  # e.g., business, tech

    def __str__(self):
        return self.name


# Attendee Model
class Attendee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Employee
    event = models.ForeignKey(Event, related_name='attendees', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} ({self.event.name})"
class Employee(models.Model):
    ROLE_CHOICES = [
        ('Manager', 'Manager'),
        ('Staff', 'Staff'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.role})"

# Task Model
class Task(models.Model):
    attendee = models.ForeignKey(Attendee, related_name='tasks', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    progress = models.IntegerField(default=0)  # 0-100%
    due_date = models.DateField()
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='tasks')

    status = models.CharField(max_length=20, choices=[
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed')
    ], default='Not Started')

    def __str__(self):
        return f"Task for {self.attendee.name}: {self.name}"


# Attendance Model
class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Employee
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[
        ('Present', 'Present'),
        ('Absent', 'Absent')
    ])
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.status}"


