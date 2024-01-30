from django.shortcuts import render
from app.models import *
# Create your views here.
def equijoins(request):
    EMPOBJECTS=Employee.objects.select_related('deptno').all()
    EMPOBJECTS=Employee.objects.select_related('deptno').filter(hiredate__year=2024)
    EMPOBJECTS=Employee.objects.select_related('deptno').filter(deptno=10)
    EMPOBJECTS=Employee.objects.select_related('deptno').filter(deptno__dname='RESEARCH')
    EMPOBJECTS=Employee.objects.select_related('deptno').filter(deptno__dloc='CHICAGO')
    EMPOBJECTS=Employee.objects.select_related('deptno').filter(mgr__isnull=True)
    EMPOBJECTS=Employee.objects.select_related('deptno').filter(comm__isnull=True)
    EMPOBJECTS=Employee.objects.select_related('deptno').filter(comm__isnull=False)
    EMPOBJECTS=Employee.objects.select_related('deptno').filter(deptno=10,sal__gt=2500)
    EMPOBJECTS=Employee.objects.select_related('deptno').all()[:5:]
    EMPOBJECTS=Employee.objects.select_related('deptno').all()[2:5:]
    EMPOBJECTS=Employee.objects.select_related('deptno').all()
    
    d={'Empobjects':EMPOBJECTS}
    return render(request,'equijoins.html',d)