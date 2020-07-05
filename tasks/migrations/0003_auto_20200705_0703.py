# Generated by Django 3.0.8 on 2020-07-05 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20200705_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterOrderWithRespectTo(
            name='task',
            order_with_respect_to='created_at',
        ),
    ]
