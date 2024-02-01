from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
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

def selfjoin(request):
    Empmgrobjects = Employee.objects.select_related('mgr').all()
    Empmgrobjects = Employee.objects.select_related('mgr').filter(ename='MARTIN')
    Empmgrobjects = Employee.objects.select_related('mgr').filter(mgr__ename='KING')
    Empmgrobjects = Employee.objects.select_related('mgr').filter(sal__gte=2500)
    Empmgrobjects = Employee.objects.select_related('mgr').filter(sal__lte=3000)
    Empmgrobjects = Employee.objects.select_related('mgr').filter(ename__startswith='A')
    Empmgrobjects = Employee.objects.select_related('mgr').filter(ename__endswith='th')
    Empmgrobjects = Employee.objects.select_related('mgr').order_by('sal')
    Empmgrobjects = Employee.objects.select_related('mgr').order_by('-sal')
    Empmgrobjects = Employee.objects.select_related('mgr').filter(mgr__isnull=True)
    Empmgrobjects = Employee.objects.select_related('mgr').filter(comm__isnull=False)
    Empmgrobjects = Employee.objects.select_related('mgr').order_by(Length('empno').desc())
    Empmgrobjects = Employee.objects.select_related('mgr').filter(ename__in=('CLARK','ALLEN','JONES'))
    d={'Empmgrobjects':Empmgrobjects}
    return render(request,'selfjoin.html',d)