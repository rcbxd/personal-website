# Generated by Django 3.0.8 on 2020-07-25 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_auto_20200725_0251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='master',
            name='discord_link',
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.Category')),
            ],
        ),
        migrations.AlterField(
            model_name='skill',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.SubCategory'),
        ),
    ]
