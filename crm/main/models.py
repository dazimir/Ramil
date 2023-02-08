from pathlib import Path
from django.db import models
from django.contrib.auth.models import User
import os
from django.utils import timezone


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, upload_to='img/', verbose_name='Изображение')


# ------------------------------------------------------------------------------------


""" DB Заказчик ФЛ """


class IndCustomer(models.Model):
    date_card = models.DateField('Дата создания карточки', null=True, default=timezone.now)
    ind_last_name = models.CharField('Фамилия', max_length=50)
    ind_name_name = models.CharField('Имя', max_length=50)
    ind_first_name = models.CharField('Отчество', max_length=50)
    ind_place_of_issue = models.CharField('Место выдачи', max_length=200)
    ind_division_code = models.CharField('Код подразделения', max_length=7)
    ind_date_of_issue = models.DateField('Дата выдачи')
    # ind_date_of_birth = models.DateField('Дата рождения')
    # ind_place_of_birth = models.CharField('Место рождения', max_length=250)
    ind_registration_address = models.CharField('Адрес регистрации', max_length=250)
    ind_residential_address = models.CharField('Адрес фактический', max_length=250)
    ind_date_registration = models.DateField('Дата регистрации')
    ind_sn_passport = models.CharField('Серия и номер паспорта', max_length=15)
    ind_snils = models.CharField('Номер СНИЛС', max_length=14)

    # kodnomer = models.CharField('номер клиента', max_length=14)

    def __str__(self):
        n = str(self.ind_last_name + ' ' + self.ind_name_name + ' ' + self.ind_first_name)
        return n

    def get_absolute_url(self):
        return self.id

    class Meta:
        verbose_name = 'Заявитель ФЛ'
        verbose_name_plural = 'Заявители ФЛ'


""" DB Заказчик ЮЛ """


class URCustomer(models.Model):
    date_card = models.DateField('Дата создания карточки', null=True, default=timezone.now)
    ul_name = models.CharField('Название юр.лица', max_length=50)
    ul_inn = models.CharField('ИНН', max_length=50)
    ul_ogrn = models.CharField('ОГРН', max_length=50)
    ul_adress = models.CharField('ЮР адрес', max_length=250)
    ul_phone = models.CharField('телефон', max_length=20)
    ul_email = models.CharField('email', max_length=50)
    ul_sozdal = models.CharField('Завел карточку', max_length=50)

    def __str__(self):
        n = str(self.ul_name)
        return n

    def get_absolute_url(self):
        return self.id

    class Meta:
        verbose_name = 'Заявитель ЮРЛ'
        verbose_name_plural = 'Заявители ЮРЛ'










# ------------------------------------------------------------------------------------


""" DB Заказчик ФЛ """


class TaskObject(models.Model):
    task_connection = models.ForeignKey(IndCustomer, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Заявитель физ.лицо')
    date_card = models.DateField('Дата создания карточки', null=True, default=timezone.now)
    task_vid = models.CharField('Вид работы', max_length=50)
    task_kadnom = models.CharField('Кадастровый номер', max_length=50)
    task_address = models.CharField('Адрес объекта', max_length=250)

    task_nomdogovor = models.CharField('Номер договора', max_length=200, blank=True)
    task_datedogovor = models.DateField('Дата договора', blank=True)
    task_skandogovor = models.CharField('Ссылка на договор', max_length=250, blank=True)

    task_kontakt = models.CharField('ФИО контактного лица', max_length=50)
    task_kontakt_phone = models.CharField('Адрес фактический', max_length=60)
    task_kontakt_email = models.CharField('Email контактного лица', max_length=50, blank=True)
    task_kontakt_info = models.CharField('Пояснения', max_length=250, blank=True)

    task_skan_link1 = models.CharField('Документ 1', max_length=250, blank=True)
    task_nom_link1 = models.CharField('Номер документ 1', max_length=250, blank=True)
    task_data_link1 = models.DateField('Дата документа 1', blank=True)

    task_skan_link2 = models.CharField('Документ 2', max_length=250, blank=True)
    task_nom_link2 = models.CharField('Номер документ 2', max_length=250, blank=True)
    task_data_link2 = models.DateField('Дата документа 2', blank=True)

    task_skan_link3 = models.CharField('Документ 3', max_length=250, blank=True)
    task_nom_link3 = models.CharField('Номер документ 3', max_length=250, blank=True)
    task_data_link3 = models.DateField('Дата документа 3', blank=True)

    task_skan_link4 = models.CharField('Документ 4', max_length=250, blank=True)
    task_nom_link4 = models.CharField('Номер документ 4', max_length=250, blank=True)
    task_data_link4 = models.DateField('Дата документа 4', blank=True)

    task_skan_link5 = models.CharField('Документ 5', max_length=250, blank=True)
    task_nom_link5 = models.CharField('Номер документ 5', max_length=250, blank=True)
    task_data_link5 = models.DateField('Дата документа 5', blank=True)

    task_skan_link6 = models.CharField('Документ 6', max_length=250, blank=True)
    task_nom_link6 = models.CharField('Номер документ 6', max_length=250, blank=True)
    task_data_link6 = models.DateField('Дата документа 6', blank=True)

    task_skan_link11 = models.CharField('Документ 11', max_length=250, blank=True)
    task_nom_link11 = models.CharField('Номер документ 11', max_length=250, blank=True)
    task_data_link11 = models.DateField('Дата документа 11', blank=True)

    task_skan_link12 = models.CharField('Документ 12', max_length=250, blank=True)
    task_nom_link12 = models.CharField('Номер документ 12', max_length=250, blank=True)
    task_data_link12 = models.DateField('Дата документа 12', blank=True)

    task_skan_link13 = models.CharField('Документ 13', max_length=250, blank=True)
    task_nom_link13 = models.CharField('Номер документ 13', max_length=250, blank=True)
    task_data_link13 = models.DateField('Дата документа 13', blank=True)

    task_skan_link14 = models.CharField('Документ 14', max_length=250, blank=True)
    task_nom_link14 = models.CharField('Номер документ 14', max_length=250, blank=True)
    task_data_link14 = models.DateField('Дата документа 14', blank=True)

    task_skan_link15 = models.CharField('Документ 15', max_length=250, blank=True)
    task_nom_link15 = models.CharField('Номер документ 15', max_length=250, blank=True)
    task_data_link15 = models.DateField('Дата документа 15', blank=True)

    task_skan_link16 = models.CharField('Документ 16', max_length=250, blank=True)
    task_nom_link16 = models.CharField('Номер документ 16', max_length=250, blank=True)
    task_data_link16 = models.DateField('Дата документа 16', blank=True)

    # kodnomer = models.CharField('номер клиента', max_length=14)

    def __str__(self):
        n = str(self.task_kadnom + ' ' + self.task_address)
        return n

    def get_absolute_url(self):
        return self.id

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'
