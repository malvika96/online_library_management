# Generated by Django 2.1.3 on 2018-11-25 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20181125_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.CharField(max_length=10),
        ),
    ]
