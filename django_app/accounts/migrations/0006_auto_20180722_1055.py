# Generated by Django 2.0.7 on 2018-07-22 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='author',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
