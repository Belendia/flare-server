# Generated by Django 2.2.10 on 2020-05-09 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0011_auto_20200509_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyresult',
            name='phone_number',
            field=models.CharField(default='', max_length=20),
        ),
    ]