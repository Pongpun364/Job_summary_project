# Generated by Django 3.2.6 on 2021-12-27 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_job_work_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
            ],
        ),
    ]
