from django.contrib import admin
from .models import StudentRecord

@admin.register(StudentRecord)
class StudentRecordAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'full_name', 'course', 'year_level', 'date_registered')
