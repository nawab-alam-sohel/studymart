# Generated by Django 5.0.6 on 2024-06-28 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aiquest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=25)),
                ('c_name', models.CharField(max_length=20)),
                ('c_duration', models.IntegerField()),
                ('seat', models.IntegerField()),
            ],
        ),
    ]
