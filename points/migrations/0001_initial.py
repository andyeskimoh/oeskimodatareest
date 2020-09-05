# Generated by Django 3.1 on 2020-09-03 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('interprity', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=10)),
                ('moinkult', models.BooleanField()),
                ('manager', models.CharField(max_length=50)),
                ('street', models.BooleanField()),
                ('conserv', models.BooleanField()),
                ('addres', models.CharField(max_length=50)),
            ],
        ),
    ]