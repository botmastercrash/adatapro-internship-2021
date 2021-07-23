# Generated by Django 3.2.5 on 2021-07-18 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profile_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('profile_username', models.CharField(max_length=64, unique=True)),
                ('profile_email', models.EmailField(max_length=128, unique=True)),
                ('password_hash', models.CharField(max_length=256)),
            ],
            options={
                'managed': True,
            },
        ),
    ]