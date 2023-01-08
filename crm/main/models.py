from pathlib import Path
from django.db import models
from django.contrib.auth.models import User
import os
from django.utils import timezone

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, upload_to='img/', verbose_name='Изображение')


#------------------------------------------------------------------------------------


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

    def __str__(self):
        n = str(self.ind_last_name + ' ' + self.ind_name_name + ' ' + self.ind_first_name)
        return n

    def get_absolute_url(self):
        return self.id

    class Meta:
        verbose_name = 'Заявитель ФЛ'
        verbose_name_plural = 'Заявители ФЛ'
