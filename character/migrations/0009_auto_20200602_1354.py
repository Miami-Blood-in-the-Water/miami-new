# Generated by Django 2.2.12 on 2020-06-02 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0008_merge_20200602_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='type',
            field=models.CharField(blank=True, editable=False, max_length=16, null=True),
        ),
    ]
