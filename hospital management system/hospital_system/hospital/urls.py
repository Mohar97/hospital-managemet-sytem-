from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-patient/', views.add_patient, name='add_patient'),
    path('employee-info/', views.employee_info, name='employee_info'),
    path('search-room/', views.search_room, name='search_room'),
    path('available-rooms/', views.available_rooms, name='available_rooms'),
    path('patient-info/', views.patient_info, name='patient_info'),
    path('upload-detail/', views.upload_detail, name='upload_detail'),
    path('departments/', views.departments, name='departments'),
    path('discharge/', views.discharge, name='discharge'),
    path('ambulance/', views.ambulance, name='ambulance'),
    path('view-patients/', views.view_patients, name='view_patients'),
    path('edit-patient/<int:pk>/', views.edit_patient, name='edit_patient'),
    path('delete-patient/<int:pk>/', views.delete_patient, name='delete_patient'),
    path('edit-patient/<int:pk>/', views.edit_patient, name='edit_patient'),
    path('view-employees/', views.view_employees, name='view_employees'),
    path('employees/', views.view_employees, name='view_employees'),
    path('edit-employee/<int:pk>/', views.edit_employee, name='edit_employee'),
    path('delete-employee/<int:pk>/', views.delete_employee, name='delete_employee'),
    path('add-ambulance/', views.add_ambulance, name='add_ambulance'),
    path('edit-ambulance/<int:pk>/', views.edit_ambulance, name='edit_ambulance'),
    path('delete-ambulance/<int:pk>/', views.delete_ambulance, name='delete_ambulance'),


    



]
