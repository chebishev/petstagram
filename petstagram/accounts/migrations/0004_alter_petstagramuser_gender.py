# Generated by Django 4.2.3 on 2023-07-21 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_petstagramuser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petstagramuser',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Do not show', 'Do not show')], max_length=11),
        ),
    ]
