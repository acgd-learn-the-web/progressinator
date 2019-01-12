# Generated by Django 2.1.2 on 2019-01-04 17:46

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('progress_core', '0009_auto_20181120_0030'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'course', 'verbose_name_plural': 'courses'},
        ),
        migrations.RemoveField(
            model_name='course',
            name='course_number',
        ),
        migrations.RemoveField(
            model_name='course',
            name='name',
        ),
        migrations.AddField(
            model_name='course',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]