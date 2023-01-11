from django import forms
from django.forms import ModelForm, TextInput
from .models import *
from django.contrib.auth.forms import AuthenticationForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


# --------------------------------------------------------------------------------------------------------------------------------
# создаем класс КАРТОЧКА ЗАЯВИТЕЛЯ

class InputFLForm(ModelForm):
    class Meta:
        model = IndCustomer
        fields = ['ind_last_name',
                  'ind_name_name',
                  'ind_first_name',
                  'ind_date_of_issue',
                  'ind_place_of_issue',
                  'ind_division_code',
                  'ind_sn_passport',
                  'ind_registration_address',
                  'ind_date_registration',
                  'ind_residential_address',
                  'ind_snils']
        widgets = {
            # "date_input_card": TextInput(attrs={'type': 'date',
            #                                     'class': 'form-control',
            #                                     'placeholder': 'Дата создания карточки', 'type': 'date'}),
            "ind_last_name": TextInput(attrs={
                'class': 'form-control',
                'id': 'familiya',
                'placeholder': 'Фамилия'}),

            "ind_name_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'}),

            "ind_first_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество'}),

            "ind_date_of_issue": TextInput(attrs={'type': 'date',
                                                  'class': 'form-control',
                                                  'placeholder': 'Дата выдачи', 'type': 'date'}),

            "ind_place_of_issue": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Место выдачи паспорта'}),

            "ind_division_code": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Код подразделения'}),

            "ind_sn_passport": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Серия и номер паспорта'}),

            # "ind_date_of_birth": TextInput(attrs={'type': 'date',
            #                                   'class': 'form-control',
            #                                   'placeholder': 'Дата рождения', 'type': 'date'}),

            "ind_registration_address": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес регистрации'}),

            "ind_date_registration": TextInput(attrs={'type': 'date',
                                                  'class': 'form-control',
                                                  'placeholder': 'Дата регистрации', 'type': 'date'}),

            "ind_residential_address": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес жительства'}),

            "ind_snils": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'СНИЛС'}),
        }


# --------------------------------------------------------------------------------------------------------------------------------
# создаем класс КАРТОЧКА ЗАЯВИТЕЛЯ

class InputULForm(ModelForm):
    class Meta:
        model = URCustomer
        fields = ['ul_name',
                  'ul_inn',
                  'ul_ogrn',
                  'ul_adress',
                  'ul_phone',
                  'ul_email']
        widgets = {
            # "date_input_card": TextInput(attrs={'type': 'date',
            #                                     'class': 'form-control',
            #                                     'placeholder': 'Дата создания карточки', 'type': 'date'}),
            "ul_name": TextInput(attrs={
                'class': 'form-control',
                'id': 'familiya',
                'placeholder': 'Название организации'}),

            "ul_inn": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ИНН организации'}),

            "ul_ogrn": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ОГРН организации'}),

            # "ul_adress": TextInput(attrs={'type': 'date',
            #                                       'class': 'form-control',
            #                                       'placeholder': 'Дата выдачи', 'type': 'date'}),

            "ul_adress": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес организации'}),

            "ul_phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон организации'}),

            "ul_email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email организации'}),

        }
