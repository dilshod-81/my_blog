# Generated by Django 4.0.6 on 2022-08-03 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorymodel',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
