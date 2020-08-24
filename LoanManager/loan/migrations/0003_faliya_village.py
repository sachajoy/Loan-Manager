# Generated by Django 3.0.8 on 2020-08-24 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0002_taluka'),
    ]

    operations = [
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('taluka_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.Taluka')),
            ],
        ),
        migrations.CreateModel(
            name='Faliya',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('village_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.Village')),
            ],
        ),
    ]