from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
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


def emp_mgr_dept(request):
    emd=Employee.objects.select_related('deptno','mgr').all()
    emd=Employee.objects.select_related('deptno','mgr').filter(deptno__dname='RESEARCH')
    emd=Employee.objects.select_related('deptno','mgr').filter(mgr__ename='BLAKE')
    emd=Employee.objects.select_related('deptno','mgr').filter(ename='MARTIN')
    emd=Employee.objects.select_related('deptno','mgr').filter(Q(deptno__dname='RESEARCH')| Q(mgr__ename='JOHNS'))
    emd=Employee.objects.select_related('deptno','mgr').filter(ename__startswith='S')
    emd=Employee.objects.select_related('deptno','mgr').filter(ename__endswith='TH')
    emd=Employee.objects.select_related('deptno','mgr').filter(ename__in=('SCOTT','ALLEN'))
    emd=Employee.objects.select_related('deptno','mgr').filter(sal__gte=2500)
    emd=Employee.objects.select_related('deptno','mgr').filter(job__in=('SALESMAN','MANAGER'))
    emd=Employee.objects.select_related('deptno','mgr').filter(mgr__isnull=True)
    emd=Employee.objects.select_related('deptno','mgr').filter(comm__isnull=False)
    emd=Employee.objects.select_related('deptno','mgr').filter(hiredate__year=2024)
    emd=Employee.objects.select_related('deptno','mgr').order_by('sal')
    emd=Employee.objects.select_related('deptno','mgr').all()[:5:]
    emd=Employee.objects.select_related('deptno','mgr').order_by('ename')
    emd=Employee.objects.select_related('deptno','mgr').all()[5:7]
    emd=Employee.objects.select_related('deptno','mgr').filter(Q(deptno__dloc='CHICAGO')|Q(mgr__ename='ALLEN'))
    emd=Employee.objects.select_related('deptno','mgr').filter(deptno__dname='ACCOUNTING',sal__gte=3000)
    emd=Employee.objects.select_related('deptno','mgr').filter(deptno__dname='SALES')
    emd=Employee.objects.select_related('deptno','mgr').filter(deptno__in=(10,20))
    emd=Employee.objects.select_related('deptno','mgr').filter(deptno__dloc='DALLAS',ename='SMITH')
    emd=Employee.objects.select_related('deptno','mgr').filter(deptno__gt=20)
    emd=Employee.objects.select_related('deptno','mgr').filter(sal__gt=4000)
    emd=Employee.objects.select_related('deptno','mgr').filter(comm__isnull=True)
    emd=Employee.objects.select_related('deptno','mgr').order_by('-sal')
    emd=Employee.objects.select_related('deptno','mgr').order_by(Length('job').desc())
    emd=Employee.objects.select_related('deptno','mgr').filter(ename='JONES',job='CLERK')
    emd=Employee.objects.select_related('deptno','mgr').all()[2:6:]
    emd=Employee.objects.select_related('deptno','mgr').all()

    d={'emd':emd}
    return render(request,'emp_mgr_dept.html',d)