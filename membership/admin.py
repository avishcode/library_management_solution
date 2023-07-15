from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(StudyRoom)
admin.site.register(Membership)

@admin.register(EnrollStudent)
class EnrollStudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'membership', 'room', 'amount', 'created_at']