# Generated by Django 2.1.1 on 2018-10-05 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('printapi', '0003_auto_20181005_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='folder',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='printapi.Folder'),
        ),
    ]
