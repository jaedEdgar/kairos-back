# Generated by Django 3.0.8 on 2020-07-30 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20200705_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(1, 'Is Check'), (2, 'Is Not Checked'), (3, 'Is Delete')], default=1),
        ),
    ]