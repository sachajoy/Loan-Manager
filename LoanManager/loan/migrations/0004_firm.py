# Generated by Django 3.0.8 on 2020-08-27 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0003_faliya_village'),
    ]

    operations = [
        migrations.CreateModel(
            name='Firm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('abv', models.CharField(max_length=10)),
            ],
        ),
    ]
