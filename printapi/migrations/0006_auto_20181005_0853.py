# Generated by Django 2.1.1 on 2018-10-05 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('printapi', '0005_auto_20181005_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='folder',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='printapi.Folder'),
        ),
    ]