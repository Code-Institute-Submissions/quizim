# Generated by Django 3.0.5 on 2020-04-17 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0007_auto_20200416_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='playeranswer',
            name='player',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
