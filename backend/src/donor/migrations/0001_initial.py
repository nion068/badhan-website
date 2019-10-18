# Generated by Django 2.0.2 on 2019-10-16 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodGroup',
            fields=[
                ('blood_group', models.CharField(max_length=15, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('batch', models.CharField(max_length=2)),
                ('room', models.CharField(max_length=10)),
                ('mobile', models.CharField(max_length=14)),
                ('last_donation', models.DateField()),
                ('count', models.IntegerField()),
                ('comment', models.CharField(max_length=100)),
                ('blood_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donor.BloodGroup')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donor.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('hall_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='donor',
            name='hall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donor.Hall'),
        ),
    ]
