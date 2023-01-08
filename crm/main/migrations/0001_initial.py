# Generated by Django 4.1.4 on 2023-01-04 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IndCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_card', models.DateField(default=django.utils.timezone.now, null=True, verbose_name='Дата создания карточки')),
                ('ind_last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('ind_name_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('ind_first_name', models.CharField(max_length=50, verbose_name='Отчество')),
                ('ind_place_of_issue', models.CharField(max_length=200, verbose_name='Место выдачи')),
                ('ind_division_code', models.CharField(max_length=7, verbose_name='Код подразделения')),
                ('ind_date_of_issue', models.DateField(verbose_name='Дата выдачи')),
                ('ind_date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('ind_place_of_birth', models.CharField(max_length=250, verbose_name='Место рождения')),
                ('ind_registration_address', models.CharField(max_length=250, verbose_name='Адрес регистрации')),
                ('ind_residential_address', models.CharField(max_length=250, verbose_name='Адрес проживания')),
                ('ind_date_registration', models.DateField(verbose_name='Дата регистрации')),
                ('ind_sn_passport', models.CharField(max_length=15, verbose_name='Серия и номер паспорта')),
                ('ind_snils', models.CharField(max_length=14, verbose_name='Номер СНИЛС')),
            ],
            options={
                'verbose_name': 'Заявитель ФЛ',
                'verbose_name_plural': 'Заявители ФЛ',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='img/', verbose_name='Изображение')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]