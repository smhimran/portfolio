# Generated by Django 3.0.3 on 2020-05-29 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='end',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='logo',
            field=models.ImageField(blank=True, upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='education',
            name='result',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
