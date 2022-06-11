# Generated by Django 3.2.9 on 2021-12-01 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=15, verbose_name='users fname')),
                ('lname', models.CharField(max_length=15, verbose_name='users lname')),
                ('email', models.EmailField(max_length=15, verbose_name='users email')),
                ('password', models.CharField(max_length=1500, verbose_name='users password')),
                ('dob', models.DateField(verbose_name='user dob')),
                ('gender', models.CharField(max_length=1500, verbose_name='users gender')),
            ],
        ),
    ]