# Generated by Django 2.2.7 on 2020-09-04 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ApplicationApp', '0005_auto_20200903_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backstage',
            name='link',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ApplicationApp.Other'),
        ),
    ]
