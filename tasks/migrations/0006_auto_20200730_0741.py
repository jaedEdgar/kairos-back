# Generated by Django 3.0.8 on 2020-07-30 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20200730_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(1, 'Is Not Checked'), (2, 'Is Check'), (3, 'Is Delete')], default=1),
        ),
    ]