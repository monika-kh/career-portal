# Generated by Django 2.2.7 on 2020-02-05 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active', max_length=25)),
                ('created', models.DateField()),
                ('updated', models.DateField()),
                ('deleted', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=250)),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active', max_length=25)),
                ('created', models.DateField()),
                ('updated', models.DateField()),
                ('delete', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active', max_length=25)),
                ('created', models.DateField()),
                ('updated', models.DateField()),
                ('deleted', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('public_id', models.IntegerField()),
                ('job_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('job_functions', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
                ('location', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('apply_by', models.DateField()),
                ('created', models.DateField()),
                ('updated', models.DateField()),
                ('deleted', models.DateField()),
                ('desired_skills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='technology', to='jobs.Technology')),
                ('job_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role', to='jobs.Role')),
            ],
        ),
    ]
