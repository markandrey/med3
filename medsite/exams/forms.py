from django import forms
from .models import Exam, NameOfExam, UploadFiles
from django.contrib.auth import get_user_model


class AddExamForm(forms.ModelForm):
    name = forms.ModelChoiceField(queryset=NameOfExam.objects.all(),
                                  empty_label='Выберите исследование', label='Название исследования')
    patient = forms.ModelChoiceField(queryset=get_user_model().objects.all(),
                                     empty_label='Выберите пациента', label='Пациент')

    class Meta:
        model = Exam
        fields = ['name', 'data', 'patient', 'content', 'photo']


class UploadFileForm(forms.ModelForm):

    class Meta:
        model = UploadFiles
        fields = ['file']

