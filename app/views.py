from django.shortcuts import render
from app.models import *
# Create your views here.
def equijoins(request):
    EMPOBJECTS=Employee.objects.select_related('deptno').all()
    d={'Empobjects':EMPOBJECTS}
    return render(request,'equijoins.html',d)