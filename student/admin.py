from django.contrib import admin
from student.models import Coursedetails, Studentdetails, Courseenrollment

# Register your models here.

admin.site.register(Coursedetails)

admin.site.register(Studentdetails)

admin.site.register(Courseenrollment)
