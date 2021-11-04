# Generated by Django 3.2.9 on 2021-11-04 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=20, verbose_name='Gender')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='Name')),
                ('last_name', models.CharField(max_length=150, verbose_name='Surname')),
                ('avatar', models.ImageField(blank=True, height_field=200, upload_to='photos/%Y/%m/%d', verbose_name='Avatar', width_field=200)),
                ('email', models.EmailField(max_length=250, verbose_name='Email')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='meet.gender', verbose_name='Gender')),
            ],
        ),
    ]