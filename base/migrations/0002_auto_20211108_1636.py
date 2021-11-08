# Generated by Django 2.2.1 on 2021-11-08 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='branch',
            field=models.CharField(blank=True, choices=[('COMPUTER SCIENCE AND ENGINEERING', 'Computer Science and Engineering'), ('ELECTRONICS ENGINEERING', 'Electronics Engineering'), ('ELECTRICAL ENGINEERING', 'Electrical Engineering'), ('MATHEMATICS AND COMPUTING', 'Mathematics and Computing'), ('MECHANICAL ENGINEERING', 'Mechanical Engineering'), ('CIVIL ENGINEERING', 'Civil Engineering'), ('CHEMICAL ENGINEERING', 'Chemical Engineering'), ('MINING ENGINEERING', 'Mining Engineering'), ('CEREMIC ENGINEERING', 'Ceremic Engineering'), ('ARCHITECTURE ENGINEERING', 'Architecture Engineering'), ('BIOCHEMICAL ENGINEERING', 'Biochemical Engineering'), ('PHARMACEUTICAL ENGINEERING', 'Pharmaceutical Engineering')], max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('FEMALE', 'Female'), ('MALE', 'Male')], default='Female', max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='program',
            field=models.CharField(blank=True, choices=[('B.TECH', 'B.Tech'), ('M.TECH', 'M.Tech'), ('PHD', 'PhD')], default='B.Tech', max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='year',
            field=models.PositiveIntegerField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', null=True),
        ),
    ]
