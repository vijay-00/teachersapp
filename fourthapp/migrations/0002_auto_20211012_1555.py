# Generated by Django 2.1.15 on 2021-10-12 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fourthapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loandetails',
            old_name='user_id',
            new_name='userid',
        ),
    ]
