from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, TemplateView, ListView

from .forms import AddExamForm, UploadFileForm
from .models import Exam, UploadFiles, Analysis
from .utils import menu, DataMixin


class First(DataMixin, TemplateView):
    template_name = 'exams/index.html'
    title_page = 'Главная страница'
    message = f"Добро пожаловать на сайт! Уже зарегистрировано {auth.get_user_model().objects.count()} участников!"


def show_all(request):
    all_exams = Exam.objects.filter(patient=request.user.pk)
    all_ans = Analysis.objects.filter(patient=request.user.pk)

    data = {
        'title': 'Вся медицинская информация.',
        'menu': menu,
        "all_exams": all_exams,
        "all_ans": all_ans,
    }
    return render(request,"exams/show_all.html", context=data)


def show_exam(request, exam_id):
    return HttpResponse(f'<h1>Результат по исследованию</h1><p> с id: {exam_id}</p>')


def show_category(request, cat_id):
    data = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'data_db': data_db,
        'cat_selected':cat_id,
    }
    return render(request, 'exams/index.html', context=data)


def info(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fp = UploadFiles(file=form.cleaned_data['file'], patient=request.user)
            fp.save()
    else:
        form = UploadFileForm()

    data = {
        'title': 'Добавление результата',
        'menu': menu,
        'form': form,
    }
    return render(request, 'exams/file_upload.html', context=data)


def about(request):
    data = {
        'title': 'О сайте',
        'menu': menu,
    }
    return render(request, 'exams/about.html', context=data)


# class AddExam(DataMixin, FormView):
#     form_class = AddExamForm
#     template_name = 'exams/addexam.html'
#     success_url = reverse_lazy('home')
#     title_page = 'Добавление результата исследования'
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
#
#
# class AddAnalysis(DataMixin, CreateView):
#     model = Analysis
#     fields = '__all__'
#     template_name = 'exams/addexam.html'
#     success_url = reverse_lazy('home')
#     title_page = 'Добавление результата анализа'
