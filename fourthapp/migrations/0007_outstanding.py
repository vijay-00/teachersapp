# Generated by Django 2.2 on 2021-10-20 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fourthapp', '0006_transactions'),
    ]

    operations = [
        migrations.CreateModel(
            name='outstanding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=30)),
                ('lop', models.CharField(max_length=30)),
                ('los', models.CharField(max_length=30)),
                ('td', models.CharField(max_length=30)),
                ('share', models.CharField(max_length=20)),
            ],
        ),
    ]
