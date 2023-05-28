# Generated by Django 4.1.5 on 2023-01-26 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaseBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_full_name', models.CharField(max_length=200, verbose_name='ФИО')),
                ('person_post', models.CharField(max_length=100, verbose_name='Должность')),
                ('person_work', models.TextField(verbose_name='Дела')),
                ('person_deadline', models.DateTimeField(verbose_name='Срок выполнения')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300, verbose_name='Комментарий')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CaseBoard.caseboard')),
            ],
        ),
    ]
