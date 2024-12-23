from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("register/", views.register, name="register"),
    path("", views.login_view, name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('employee_dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('event/create/', views.create_event, name='create_event'),
    path('event/edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('event/delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('event/<int:event_id>/attendees/', views.manage_attendees, name='manage_attendees'),
    path('event/<int:event_id>/attendee/create/', views.create_attendee, name='create_attendee'),
    path('attendee/<int:attendee_id>/tasks/', views.manage_tasks, name='manage_tasks'),
    path('attendee/<int:attendee_id>/task/create/', views.create_task, name='create_task'),
    path('attendance/', views.mark_attendance, name='mark_attendance'),
    path('task/<int:task_id>/complete/', views.mark_task_completed, name='mark_task_completed'),
    path('assign_task/', views.assign_task, name='assign_task'),


]
