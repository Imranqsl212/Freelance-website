# Generated by Django 4.2.4 on 2023-08-28 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_apply_vacansy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='room',
        ),
        migrations.AlterField(
            model_name='apply',
            name='vacansy',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='base.vacansy'),
        ),
    ]
