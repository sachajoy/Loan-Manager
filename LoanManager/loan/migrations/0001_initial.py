<<<<<<< HEAD
# Generated by Django 3.0.8 on 2020-08-19 11:54
=======
# Generated by Django 3.0.8 on 2020-08-20 18:04
>>>>>>> address

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
