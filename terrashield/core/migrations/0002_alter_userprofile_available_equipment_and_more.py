# Generated by Django 5.1 on 2024-08-28 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='available_equipment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='fitness_goal',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
