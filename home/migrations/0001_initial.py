# Generated by Django 3.1.1 on 2021-05-31 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('des', models.CharField(max_length=500)),
                ('email', models.CharField(default='abdulrehmankalsekar@gmail.com', max_length=500)),
                ('complete_in', models.IntegerField()),
            ],
        ),
    ]
