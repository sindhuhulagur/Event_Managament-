from asyncio import Task
from datetime import timezone
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Attendee, Employee, Event
from .forms import AttendanceForm, AttendeeForm, EventForm, TaskForm
from django.contrib.auth.decorators import login_required
from .models import Event, Attendee, Task, Attendance
from django.contrib.auth.views import LoginView

# User Registration View
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

# User Login View
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

# User Logout View

def dashboard(request):
    # Get category filter from query parameters
    category = request.GET.get('category')  
    
    # Filter events by user and optional category
    if category:
        events = Event.objects.filter(user=request.user, category=category)
    else:
        events = Event.objects.filter(user=request.user)
    
    # Get tasks and attendance related to the logged-in user
    tasks = Task.objects.filter(attendee__user=request.user)
    attendance = Attendance.objects.filter(user=request.user)
    
    # Render the dashboard template with context data
    return render(request, 'dashboard.html', {
        'events': events,
        'tasks': tasks,
        'attendance': attendance,
        'selected_category': category  # Optional: To keep track of the selected category in the UI
    })
    
    
# Mark Attendance
@login_required
def mark_attendance(request):
    if request.method == 'POST':
        status = request.POST['status']
        comment = request.POST.get('comment', '')
        Attendance.objects.create(user=request.user, date=request.POST['date'], status=status, comment=comment)
        return redirect('dashboard')
    return render(request, 'mark_attendance.html')

# Task Completion
@login_required
def mark_task_completed(request, task_id):
    task = Task.objects.get(id=task_id, attendee__user=request.user)
    task.status = 'Completed'
    task.progress = 100
    task.save()
    return redirect('dashboard')


def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user  # Assign the current user as the event creator
            event.save()
            return redirect('dashboard')
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})

def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, user=request.user)  # Ensure the user can only edit their events
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EventForm(instance=event)
    return render(request, 'edit_event.html', {'form': form, 'event': event})

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, user=request.user)
    event.delete()
    return redirect('dashboard')

def manage_attendees(request, event_id):
    event = get_object_or_404(Event, id=event_id, user=request.user)
    attendees = Attendee.objects.filter(event=event)
    return render(request, 'manage_attendees.html', {'event': event, 'attendees': attendees})

def create_attendee(request, event_id):
    event = get_object_or_404(Event, id=event_id, user=request.user)
    if request.method == 'POST':
        form = AttendeeForm(request.POST)
        if form.is_valid():
            attendee = form.save(commit=False)
            attendee.event = event  # Link the attendee to the current event
            attendee.save()
            return redirect('manage_attendees', event_id=event.id)
    else:
        form = AttendeeForm()
    return render(request, 'create_attendee.html', {'form': form, 'event': event})

def manage_tasks(request, attendee_id):
    attendee = get_object_or_404(Attendee, id=attendee_id)
    tasks = Task.objects.filter(attendee=attendee)
    return render(request, 'manage_tasks.html', {'attendee': attendee, 'tasks': tasks})

def create_task(request, attendee_id):
    attendee = get_object_or_404(Attendee, id=attendee_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.attendee = attendee  # Assign task to the selected attendee
            task.save()
            return redirect('manage_tasks', attendee_id=attendee.id)
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form, 'attendee': attendee})

def logout_view(request):
    logout(request)
    return redirect("login")

def assign_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('task_list')  # Redirect to a task list or another page as needed
    else:
        form = TaskForm()

    return render(request, 'employee_dashboard/assign_task.html', {'form': form})

def mark_attendance(request):
    employee = Employee.objects.get(user=request.user)  # Assuming the logged-in user is an employee
    today = timezone.now().date()

    # Check if attendance for today has already been marked
    if Attendance.objects.filter(user=employee.user, date=today).exists():
        return redirect('attendance_success')  # Redirect if already marked attendance

    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.user = employee.user
            attendance.date = today
            attendance.save()
            return redirect('attendance_success')  # Redirect to a success page or list
    else:
        form = AttendanceForm()

    return render(request, 'employee_dashboard/mark_attendance.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Specify the login template if needed

    def get_redirect_url(self):
        # Check if the logged-in user is an employee and redirect accordingly
        if hasattr(self.request.user, 'employee'):  # If the user is an employee
            return reverse_lazy('employee_dashboard')
        else:  # If the user is a regular user
            return reverse_lazy('user_dashboard')  
        
def employee_dashboard(request):
    # Logic for employee dashboard
    return render(request, 'employee_dashboard/dashboard.html')