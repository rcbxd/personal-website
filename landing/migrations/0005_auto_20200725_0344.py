# Generated by Django 3.0.8 on 2020-07-25 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_auto_20200725_0311'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='has_subcategory',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='has_subskill',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='has_skill',
            field=models.BooleanField(default=True),
        ),
    ]
