# Generated by Django 3.1 on 2020-08-08 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=10000)),
                ('name', models.CharField(max_length=10000)),
                ('email', models.CharField(max_length=10000)),
                ('address', models.CharField(max_length=10000)),
                ('city', models.CharField(max_length=10000)),
                ('state', models.CharField(max_length=10000)),
                ('zipcode', models.CharField(max_length=10000)),
            ],
        ),
    ]
