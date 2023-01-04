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
        fields = ['date_card', 'ind_last_name', 'ind_name_name', 'ind_first_name', 'ind_place_of_issue',
                  'ind_division_code',
                  'ind_date_of_issue', 'ind_date_of_birth', 'ind_place_of_birth', 'ind_registration_address',
                  'ind_residential_address', 'ind_sn_passport', 'ind_date_registration', 'ind_snils']
        widgets = {
            "date_input_card": TextInput(attrs={'type': 'date',
                                                'class': 'form-control',
                                                'placeholder': 'Дата создания карточки', 'type': 'date'}),

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

            "ind_place_of_issue": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Место выдачи паспорта'}),

            "ind_division_code": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Код подразделения'}),

            "ind_date_of_issue": TextInput(attrs={'type': 'date',
                                              'class': 'form-control',
                                              'placeholder': 'Дата выдачи', 'type': 'date'}),

            "ind_date_of_birth": TextInput(attrs={'type': 'date',
                                              'class': 'form-control',
                                              'placeholder': 'Дата рождения', 'type': 'date'}),

            "ind_registration_address": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес регистрации'}),

            "ind_date_registration": TextInput(attrs={'type': 'date',
                                                  'class': 'form-control',
                                                  'placeholder': 'Дата регистрации', 'type': 'date'}),

            "ind_residential_address": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес жительства'}),

            "ind_sn_passport": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Серия и номер паспорта'}),

            "ind_snils": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'СНИЛС'}),

            "ind_card_search": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО карточки заявителя для поиска'}),
        }
