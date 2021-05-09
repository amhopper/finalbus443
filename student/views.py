from django.shortcuts import render
from django.http import HttpResponse
from student.models import Studentdetails, Coursedetails, Courseenrollment
from django.db import connection
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.db.models import Count


# Create your views here.

@login_required
def home(request):
    enrolled = Studentdetails.objects.count()
    coursesoffered = Coursedetails.objects.count()
    avggpa = Studentdetails.objects.all().aggregate(Avg('gpa'))
    numbersophomores = Studentdetails.objects.filter(year='Sophomore').count()
    numberjuniors = Studentdetails.objects.filter(year='Junior').count()
    numberseniors = Studentdetails.objects.filter(year='Senior').count()
    context = {'enrolled':enrolled, 'coursesoffered':coursesoffered, 'avggpa':avggpa, 'numbersophomores':numbersophomores, 'numberjuniors':numberjuniors, 'numberseniors': numberseniors}
    return render(request, 'student/home.html', context,)

@login_required
def studentdetails(request):
    studentdata = Studentdetails.objects.all()
    paginator = Paginator(studentdata, 10)
    page = request.GET.get('page')
    minidata = paginator.get_page(page)
    context = {'data':minidata}
    return render(request, 'student/studentdetails.html', context)

@login_required
def coursedetails(request):
    coursedata = Coursedetails.objects.all()
    paginator = Paginator(coursedata, 10)
    page = request.GET.get('page')
    minidata = paginator.get_page(page)
    context = {'data':minidata}
    return render(request, 'student/coursedetails.html', context)

@login_required
def enrollment(request):
    studentdata = Studentdetails.objects.all()
    coursedata = Coursedetails.objects.all()
    enrollmentdata = Courseenrollment.objects.all()
    paginator = Paginator(enrollmentdata, 10)
    page = request.GET.get('page')
    minidata = paginator.get_page(page)
    context = {'student':studentdata, 'course':coursedata, 'data':minidata}
    return render(request, 'student/studentenrollment.html', context)

@login_required
def saveenrollment(request):
    studentid = request.GET.get('studentid')
    coursename = request.GET.get('coursename')
    coursecount = Courseenrollment.objects.filter(studentid=studentid).count()
    courses = Courseenrollment.objects.values_list('coursename', flat=True).filter(studentid=studentid)
    if(coursecount < 3):
        if(coursename not in courses):
            dataobj = Courseenrollment(studentid = studentid, coursename = coursename)
            dataobj.save()
    else:
        HttpResponse("Error with student enrollment")
    return HttpResponse("Success")

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
