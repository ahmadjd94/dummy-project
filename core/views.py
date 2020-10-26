from django.shortcuts import render, redirect

# Create your views here.
from .forms import EmployeeForm
from .models import Employee


def employees_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = EmployeeForm()

    return render(request, 'new_employee.html', {'form': form})


def employees(request):
    context = {"employees": Employee.objects.all()}
    return render(request, 'employee.html', context)
