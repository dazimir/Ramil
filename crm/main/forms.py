from django import forms
from django.forms import ModelForm, TextInput, CharField
from .models import *
from django.contrib.auth.forms import AuthenticationForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


# --------------------------------------------------------------------------------------------------------------------------------
# создаем класс КАРТОЧКА ЗАЯВИТЕЛЯ ФЛ

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
# создаем класс КАРТОЧКА ЗАЯВИТЕЛЯ ЮЛ

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



# --------------------------------------------------------------------------------------------------------------------------------
# создаем класс КАРТОЧКА ОБЪЕКТА

class InputObjectCardForm(ModelForm):
    class Meta:
        model = TaskObject
        fields = ['task_connection', 'task_vid', 'task_kadnom', 'task_address',
                  'task_nomdogovor', 'task_datedogovor', 'task_skandogovor',
                  'task_kontakt', 'task_kontakt_phone', 'task_kontakt_email', 'task_kontakt_info',
                  'task_skan_link1', 'task_nom_link1', 'task_data_link1',
                  'task_skan_link2', 'task_nom_link2', 'task_data_link2',
                  'task_skan_link3', 'task_nom_link3', 'task_data_link3',
                  'task_skan_link4', 'task_nom_link4', 'task_data_link4',
                  'task_skan_link5', 'task_nom_link5', 'task_data_link5',
                  'task_skan_link6', 'task_nom_link6', 'task_data_link6',
                  'task_skan_link11', 'task_nom_link11', 'task_data_link11',
                  'task_skan_link12', 'task_nom_link12', 'task_data_link12',
                  'task_skan_link13', 'task_nom_link13', 'task_data_link13',
                  'task_skan_link14', 'task_nom_link14', 'task_data_link14',
                  'task_skan_link15', 'task_nom_link15', 'task_data_link15',
                  'task_skan_link16', 'task_nom_link16', 'task_data_link16'
                  ]
        widgets = {
            "task_connection": TextInput(attrs={
                'class': 'form-select',
                'id': 'zakazchik',
                'placeholder': 'Выбери заказчика'}),

            "task_vid": TextInput(attrs={
                'class': 'form-select',
                'placeholder': 'Выбири вид работ'}),

            "task_kadnom": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Кадастровый номер'}),

            "task_address": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес объекта'}),

            "task_nomdogovor": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер договора'}),

            "task_datedogovor": TextInput(attrs={'type': 'date',
                                                  'class': 'form-control',
                                                  'placeholder': 'Дата договора', 'type': 'date'}),

            "task_skandogovor": TextInput(attrs={
                'type': 'file',
                'class': 'form-control',
                'placeholder': 'Скан договора'}),

            "task_kontakt": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО контактного лица'}),

            "task_kontakt_phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон контактного лица'}),

            "task_kontakt_email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email контактного лица'}),

            "task_kontakt_info": CharField(attrs={
                'class': 'form-control',
                'placeholder': 'Дополнительная информация'}),


            "task_skan_link1": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Приложенный документ'}),
            "task_nom_link1": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер документа'}),
            "task_data_link1": TextInput(attrs={'type': 'date',
                                                  'class': 'form-control',
                                                  'placeholder': 'Дата документа', 'type': 'date'}),
            "task_skan_link2": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Приложенный документ'}),
            "task_nom_link2": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер документа'}),
            "task_data_link2": TextInput(attrs={'type': 'date',
                                                'class': 'form-control',
                                                'placeholder': 'Дата документа', 'type': 'date'}),
            "task_skan_link3": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Приложенный документ'}),
            "task_nom_link3": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер документа'}),
            "task_data_link3": TextInput(attrs={'type': 'date',
                                                'class': 'form-control',
                                                'placeholder': 'Дата документа', 'type': 'date'}),
            "task_skan_link4": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Приложенный документ'}),
            "task_nom_link4": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер документа'}),
            "task_data_link4": TextInput(attrs={'type': 'date',
                                                'class': 'form-control',
                                                'placeholder': 'Дата документа', 'type': 'date'}),
            "task_skan_link5": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Приложенный документ'}),
            "task_nom_link5": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер документа'}),
            "task_data_link5": TextInput(attrs={'type': 'date',
                                                'class': 'form-control',
                                                'placeholder': 'Дата документа', 'type': 'date'}),
            "task_skan_link6": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Приложенный документ'}),
            "task_nom_link6": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер документа'}),
            "task_data_link6": TextInput(attrs={'type': 'date',
                                                'class': 'form-control',
                                                'placeholder': 'Дата документа', 'type': 'date'}),



            "task_skan_link11": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Приложенный документ'}),
            "task_nom_link11": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер документа'}),
            "task_data_link11": TextInput(attrs={'type': 'date',
                                                'class': 'form-control',
                                                'placeholder': 'Дата документа', 'type': 'date'}),
            "task_skan_link12": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Приложенный документ'}),
            "task_nom_link12": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер документа'}),
            "task_data_link12": TextInput(attrs={'type': 'date',
                                                 'class': 'form-control',
                                                 'placeholder': 'Дата документа', 'type': 'date'}),
            "task_skan_link13": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Приложенный документ'}),
            "task_nom_link13": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер документа'}),
            "task_data_link13": TextInput(attrs={'type': 'date',
                                                 'class': 'form-control',
                                                 'placeholder': 'Дата документа', 'type': 'date'}),
            "task_skan_link14": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Приложенный документ'}),
            "task_nom_link14": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер документа'}),
            "task_data_link14": TextInput(attrs={'type': 'date',
                                                 'class': 'form-control',
                                                 'placeholder': 'Дата документа', 'type': 'date'}),
            "task_skan_link15": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Приложенный документ'}),
            "task_nom_link15": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер документа'}),
            "task_data_link15": TextInput(attrs={'type': 'date',
                                                 'class': 'form-control',
                                                 'placeholder': 'Дата документа', 'type': 'date'}),
            "task_skan_link16": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Приложенный документ'}),
            "task_nom_link16": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер документа'}),
            "task_data_link16": TextInput(attrs={'type': 'date',
                                                 'class': 'form-control',
                                                 'placeholder': 'Дата документа', 'type': 'date'}),

        }