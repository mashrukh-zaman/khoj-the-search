# Generated by Django 4.1.3 on 2022-11-11 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_value_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='value',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='value',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]
