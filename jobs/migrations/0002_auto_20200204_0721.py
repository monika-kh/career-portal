# Generated by Django 2.2.7 on 2020-02-04 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='job_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='public_id',
            field=models.IntegerField(),
        ),
    ]
