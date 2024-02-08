from django.contrib import admin
from .models import Exam, NameOfExam, NameOfAnalysis, GroupOfAnalysis, Analysis


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['name', 'data', 'patient', 'content']


admin.site.register(NameOfAnalysis)
admin.site.register(NameOfExam)
admin.site.register(GroupOfAnalysis)
admin.site.register(Analysis)

