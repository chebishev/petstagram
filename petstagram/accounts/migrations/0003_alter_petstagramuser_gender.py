# Generated by Django 4.2.3 on 2023-07-21 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_petstagramuser_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petstagramuser',
            name='gender',
            field=models.CharField(choices=[('Male', 'MALE'), ('Female', 'FEMALE'), ('Do not show', 'DO_NOT_SHOW')], max_length=11),
        ),
    ]
