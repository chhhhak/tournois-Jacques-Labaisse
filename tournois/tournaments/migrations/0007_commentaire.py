# Generated by Django 4.2 on 2023-04-20 18:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0006_alter_match_goals1_alter_match_goals2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Posted on')),
                ('text', models.CharField(max_length=500)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.match')),
            ],
        ),
    ]
