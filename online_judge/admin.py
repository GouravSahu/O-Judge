from django.contrib import admin

# Register your models here.

from . models import Problems,Testcase
admin.site.register(Problems)
admin.site.register(Testcase)