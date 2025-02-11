# Generated by Django 5.1.3 on 2024-12-08 16:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=255, null=True)),
                ('fee', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=255, null=True)),
                ('student_address', models.CharField(max_length=255, null=True)),
                ('student_age', models.IntegerField(blank=True, null=True)),
                ('joining_date', models.DateField(null=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student_app.course')),
            ],
        ),
    ]
