# Generated by Django 3.2.4 on 2022-05-20 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=500)),
                ('link', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
                ('img', models.CharField(max_length=900)),
                ('iframe', models.CharField(max_length=2)),
            ],
        ),
    ]