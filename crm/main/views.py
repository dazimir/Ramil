from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django import forms
from django.urls import reverse_lazy

from .forms import LoginUserForm, InputFLForm
from .models import *

from django.shortcuts import render


def admin(request):
    return render(request, '/admin')


def index(request):
    return render(request, 'main/index.html')


# def login(request):
#     return render(request, 'main/login.html')


# ======================================================================================
def zayavlenie(request):
    return render(request, 'main/zayavitel.html')


def zayavlenie_FL(request):
    return render(request, 'main/zayavitel_FL.html')


def zayavlenie_UL(request):
    return render(request, 'main/zayavitel_UL.html')


def zayavlenie_GOS(request):
    return render(request, 'main/zayavitel_GOS.html')


# ======================================================================================
def objects_card(request):
    return render(request, 'main/objects_card.html')


def objects_list(request):
    return render(request, 'main/objects_list.html')


def objects_search(request):
    return render(request, 'main/objects_search.html')


def objects_registration(request):
    return render(request, 'main/objects_registration.html')


# ======================================================================================
def statistik(request):
    return render(request, 'main/statistik.html')


def statistik_operator(request):
    return render(request, 'main/statistik_operator.html')


def statistik_works(request):
    return render(request, 'main/statistik_works.html')


def statistik_analiz(request):
    return render(request, 'main/statistik_analiz.html')


# ======================================================================================
def print_o(request):
    return render(request, 'main/print.html')


def print_report(request):
    return render(request, 'main/print_report.html')


def print_doc(request):
    return render(request, 'main/print_doc.html')


# ======================================================================================
def operators(request):
    return render(request, 'main/operators.html')


def settings(request):
    return render(request, 'main/settings.html')


def sites(request):
    return render(request, 'main/sites.html')


# ======================================================================================
class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'
    print("мы тута =================================================================")

    def get_context_data(self, *, object_list=None, **kwargs):
        print('2 тута =================================================================')
        context = super().get_context_data(**kwargs)

        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('login')


# --------------------------------------------------------------------------------------------------------------------
def zayavlenie_FL(request):
    error = ''
    print('=====1=======')
    if request.method == 'POST':
        print('===== если POST =======')
        form = InputFLForm(request.POST)
        if form.is_valid():
            form.save()
            print('==== если валид =======')
            return redirect('/')
        else:
            error = 'Поля заполнены не верно'
    form = InputFLForm()
    context = {
        'form': form,
        'error': error,
        'page_title': 'Ввод данных заявителя, физическое лицо',
        'temp': 'НОВАЯ'
    }
    return render(request, 'main/zayavitel_FL.html', context)


# ======================================================================================


def spisok_zayavit_FL(request):
    if request.method == 'GET':
        cards = IndCustomer.objects.order_by('-id')
        print('------ это GET  -------')
        return render(request, 'main/spisok_zayavit_FL.html',
                      {'title2': 'Карточка', 'cards': cards})  # выводим все карточки

