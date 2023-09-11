# Generated by Django 4.2.5 on 2023-09-11 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateTimeField()),
                ('type_position', models.BooleanField()),
                ('currency', models.CharField(max_length=20)),
                ('entry_price', models.IntegerField()),
                ('dollar_value', models.IntegerField()),
                ('coin_value', models.IntegerField()),
                ('notes', models.CharField(default=None, max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]