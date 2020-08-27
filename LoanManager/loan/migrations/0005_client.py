# Generated by Django 3.0.8 on 2020-08-27 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0004_firm'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challan_no', models.IntegerField(unique=True)),
                ('file_no', models.CharField(max_length=15, unique=True)),
                ('fname', models.CharField(max_length=50)),
                ('mname', models.CharField(max_length=50, null=True)),
                ('lname', models.CharField(max_length=50)),
                ('addr', models.CharField(max_length=255)),
                ('mob_no', models.CharField(max_length=11)),
                ('gtr', models.CharField(max_length=100)),
                ('gtr_mob_no', models.CharField(max_length=11)),
                ('faliya', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.Faliya')),
                ('firm_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.Firm')),
            ],
        ),
    ]
