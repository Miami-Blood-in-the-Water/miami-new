# Generated by Django 2.2.12 on 2020-06-02 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0009_auto_20200602_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
