# Generated by Django 2.0.2 on 2018-02-19 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='img',
            field=models.FileField(upload_to='personal/static/personal/img/'),
        ),
    ]
