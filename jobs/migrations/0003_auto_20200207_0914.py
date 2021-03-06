# Generated by Django 2.2.7 on 2020-02-07 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20200207_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='public_id',
            field=models.BigIntegerField(editable=False, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='public_id',
            field=models.BigIntegerField(editable=False, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='subscribers',
            name='public_id',
            field=models.BigIntegerField(editable=False, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='technicalskills',
            name='public_id',
            field=models.BigIntegerField(editable=False, null=True, unique=True),
        ),
    ]
