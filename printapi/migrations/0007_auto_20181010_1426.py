# Generated by Django 2.1.1 on 2018-10-10 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printapi', '0006_auto_20181005_0853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='creation',
        ),
        migrations.RemoveField(
            model_name='file',
            name='name',
        ),
        migrations.AddField(
            model_name='file',
            name='file',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
