# Generated by Django 3.0.8 on 2020-07-05 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterOrderWithRespectTo(
            name='notebook',
            order_with_respect_to='created_at',
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.IntegerField(choices=[(1, 'Is Check'), (2, 'Is Not Checked'), (3, 'Is Delete')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('notebook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Notebook')),
            ],
        ),
    ]