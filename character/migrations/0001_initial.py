# Generated by Django 2.2.12 on 2020-05-16 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('objects', '0011_auto_20191025_0831'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('character', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='objects.ObjectDB')),
            ],
        ),
    ]
