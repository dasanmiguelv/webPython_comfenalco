# Generated by Django 4.0.4 on 2022-05-10 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type_dish', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=500)),
            ],
        ),
    ]
