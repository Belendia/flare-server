# Generated by Django 2.2.10 on 2020-05-03 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0008_channel_messages'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('message', '0007_auto_20200502_0504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='status',
        ),
        migrations.CreateModel(
            name='MessageStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('status_success', models.IntegerField()),
                ('status_error', models.IntegerField(null=True)),
                ('configuration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.Configuration')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_messagestatus', to=settings.AUTH_USER_MODEL)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='message.Message')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_messagestatus', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='message',
            name='status',
            field=models.ManyToManyField(blank=True, through='message.MessageStatus', to='settings.Configuration'),
        ),
    ]
