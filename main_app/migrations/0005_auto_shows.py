# Generated by Django 2.1.7 on 2019-03-16 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20190316_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='shows',
            field=models.ManyToManyField(to='main_app.Show'),
        ),
    ]