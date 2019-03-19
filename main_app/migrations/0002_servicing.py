# Generated by Django 2.1.7 on 2019-03-15 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('service', models.CharField(choices=[('C', 'car wash'), ('G', 'gas'), ('B', 'body work')], default='C', max_length=1)),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Auto')),
            ],
        ),
    ]
