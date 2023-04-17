# Generated by Django 4.2 on 2023-04-17 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournoi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('beg_date', models.DateTimeField(verbose_name='Date began')),
                ('end_date', models.DateTimeField(verbose_name='Date ended')),
            ],
        ),
    ]
