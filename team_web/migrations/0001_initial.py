# Generated by Django 4.2.7 on 2023-11-27 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('role', models.CharField(choices=[('Admin', 'Admin'), ('Regular', 'Regular Team Member')], max_length=20)),
            ],
        ),
    ]