# Generated by Django 3.1.1 on 2021-05-31 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='email',
            field=models.CharField(blank=True, default='abdulrehmankalsekar@gmail.com', max_length=500),
        ),
    ]
