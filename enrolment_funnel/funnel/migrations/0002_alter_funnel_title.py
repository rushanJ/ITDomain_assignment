# Generated by Django 5.0.1 on 2024-01-07 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funnel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funnel',
            name='title',
            field=models.CharField(blank=True, default='', max_length=100, unique=True),
        ),
    ]