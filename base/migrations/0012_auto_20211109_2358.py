# Generated by Django 2.2.1 on 2021-11-09 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_notifications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='date_notif',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]