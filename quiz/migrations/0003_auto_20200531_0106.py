# Generated by Django 3.0.5 on 2020-05-31 00:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20200526_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playeranswer',
            name='id',
            field=models.UUIDField(default=uuid.UUID('c84163e8-0cea-41a5-8c0a-69b37103fd68'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.UUIDField(default=uuid.UUID('62726c56-47c6-463a-88a7-d70538bfc448'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='id',
            field=models.UUIDField(default=uuid.UUID('208f8672-036d-45c4-8538-5e088ddc4b2d'), editable=False, primary_key=True, serialize=False),
        ),
    ]
