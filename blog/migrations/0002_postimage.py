# Generated by Django 3.0.8 on 2020-08-05 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BlogPost')),
            ],
        ),
    ]
