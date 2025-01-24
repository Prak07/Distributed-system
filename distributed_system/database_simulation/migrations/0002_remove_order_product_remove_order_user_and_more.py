# Generated by Django 4.2.3 on 2025-01-24 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_simulation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='product_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]
