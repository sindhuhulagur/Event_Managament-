from django.contrib import admin
from .models import Attendee, Employee, Task

admin.site.register(Attendee)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'role', 'date_joined')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'progress', 'status', 'assigned_to')
