# Generated by Django 3.0.7 on 2020-07-07 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contr_clienti', '0002_auto_20200707_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persoanacontact',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='persoanacontact',
            name='telefon',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reprezentant',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='reprezentant',
            name='telefon',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
