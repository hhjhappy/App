# Generated by Django 2.2.7 on 2020-09-03 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ApplicationApp', '0004_auto_20200903_1425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backstage',
            name='title',
        ),
        migrations.AddField(
            model_name='backstage',
            name='link',
            field=models.ForeignKey(default=111, on_delete=django.db.models.deletion.DO_NOTHING, to='ApplicationApp.Other'),
            preserve_default=False,
        ),
    ]
