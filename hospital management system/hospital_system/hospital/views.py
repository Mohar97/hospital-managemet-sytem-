from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from django import forms
from .models import Patient, Employee, Room
from .forms import PatientForm
from .models import Department
from .models import Ambulance
from .forms import AmbulanceForm
from .models import Patient, PatientDocument

# Employee form added here
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'department', 'email', 'contact']


# ----------------- PATIENT VIEWS -----------------

@login_required
def dashboard(request):
    return render(request, 'hospital/dashboard.html')


@login_required
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_patients')
    else:
        form = PatientForm()
    return render(request, 'hospital/add_patient.html', {'form': form})


@login_required
def view_patients(request):
    query = request.GET.get('search')
    if query:
        patients = Patient.objects.filter(Q(name__icontains=query) | Q(id__icontains=query))
    else:
        patients = Patient.objects.all()
    return render(request, 'hospital/view_patients.html', {'patients': patients})


@login_required
def edit_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient updated successfully.')
            return redirect('view_patients')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'hospital/edit_patient.html', {'form': form, 'patient': patient})


@login_required
def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        messages.success(request, 'Patient deleted successfully.')
        return redirect('view_patients')
    return render(request, 'hospital/confirm_delete.html', {'patient': patient})


# ----------------- EMPLOYEE VIEWS -----------------

@login_required
def employee_info(request):
    return render(request, 'hospital/employee_info.html')


@login_required
def view_employees(request):
    employees = Employee.objects.all()
    return render(request, 'hospital/view_employees.html', {'employees': employees})


@login_required
def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee updated successfully.')
            return redirect('view_employees')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'hospital/edit_employee.html', {'form': form})


@login_required
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, 'Employee deleted successfully.')
        return redirect('view_employees')
    return render(request, 'hospital/confirm_delete_employee.html', {'employee': employee})


# ----------------- OTHER STATIC PAGE VIEWS -----------------

@login_required
def search_room(request):
    room_number = request.GET.get('room_number')
    room_type = request.GET.get('room_type')
    
    rooms = Room.objects.all()
    
    if room_number:
        rooms = rooms.filter(room_number__icontains=room_number)
    if room_type:
        rooms = rooms.filter(room_type__iexact=room_type)

    return render(request, 'hospital/search_room.html', {'rooms': rooms})

@login_required
def available_rooms(request):
    search_query = request.GET.get('search', '')
    if search_query:
        rooms = Room.objects.filter(
            Q(room_number__icontains=search_query) |
            Q(room_type__icontains=search_query)
        )
    else:
        rooms = Room.objects.all()
    return render(request, 'hospital/available_rooms.html', {'rooms': rooms})


@login_required
def patient_info(request):
    return render(request, 'hospital/patient_info.html')


@login_required
def upload_detail(request):
    if request.method == 'POST':
        patient_id = request.POST.get('patient')
        document = request.FILES.get('document')
        if patient_id and document:
            patient = Patient.objects.get(id=patient_id)
            PatientDocument.objects.create(patient=patient, document=document)
            messages.success(request, 'Document uploaded successfully.')
            return redirect('upload_detail')
        else:
            messages.error(request, 'Please fill all fields.')

    patients = Patient.objects.all()
    documents = PatientDocument.objects.all().order_by('-uploaded_at')
    return render(request, 'hospital/upload_detail.html', {'patients': patients, 'documents': documents})


@login_required
def departments(request):
    query = request.GET.get('search', '')
    if query:
        departments = Department.objects.filter(
            Q(name__icontains=query) | Q(head__icontains=query)
        )
    else:
        departments = Department.objects.all()
    return render(request, 'hospital/departments.html', {'departments': departments})


@login_required
def discharge(request):
    query = request.GET.get('search')
    if query:
        discharged_patients = Patient.objects.filter(
            Q(name__icontains=query) | Q(id__icontains=query),
            discharge_date__isnull=False
        )
    else:
        discharged_patients = Patient.objects.filter(discharge_date__isnull=False)
    return render(request, 'hospital/discharge.html', {'discharged_patients': discharged_patients})



@login_required
def ambulance(request):
    ambulances = Ambulance.objects.all()
    return render(request, 'hospital/ambulance.html', {'ambulances': ambulances})

@login_required
def add_ambulance(request):
    if request.method == 'POST':
        form = AmbulanceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ambulance added successfully.")
            return redirect('ambulance')
    else:
        form = AmbulanceForm()
    return render(request, 'hospital/add_ambulance.html', {'form': form})

@login_required
def edit_ambulance(request, pk):
    ambulance = get_object_or_404(Ambulance, pk=pk)
    if request.method == 'POST':
        form = AmbulanceForm(request.POST, instance=ambulance)
        if form.is_valid():
            form.save()
            messages.success(request, "Ambulance updated successfully.")
            return redirect('ambulance')
    else:
        form = AmbulanceForm(instance=ambulance)
    return render(request, 'hospital/edit_ambulance.html', {'form': form})

@login_required
def delete_ambulance(request, pk):
    ambulance = get_object_or_404(Ambulance, pk=pk)
    if request.method == 'POST':
        ambulance.delete()
        messages.success(request, "Ambulance deleted successfully.")
        return redirect('ambulance')
    return render(request, 'hospital/confirm_delete_ambulance.html', {'ambulance': ambulance})
