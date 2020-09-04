# Generated by Django 2.2.7 on 2020-09-02 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ApplicationApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='backstage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filesname', models.FileField(upload_to='media/', verbose_name='文件上传')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ApplicationApp.Other')),
            ],
        ),
    ]