from django.contrib import admin

# Register your models here.

from . models import Problems,Testcase, studentData
admin.site.register(Problems)
admin.site.register(Testcase)
admin.site.register(studentData)