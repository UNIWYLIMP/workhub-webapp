# Generated by Django 4.1.1 on 2023-07-08 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workapp', '0014_jobpost_job_external_jobpost_job_external_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='cover_letter',
            field=models.CharField(default='No cover letter available', max_length=5000),
        ),
    ]
