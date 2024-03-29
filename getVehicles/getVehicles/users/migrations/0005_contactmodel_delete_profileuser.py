# Generated by Django 5.0 on 2023-12-31 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profileuser_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('feedback', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='ProfileUser',
        ),
    ]
