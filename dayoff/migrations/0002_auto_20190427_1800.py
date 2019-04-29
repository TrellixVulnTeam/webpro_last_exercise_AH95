# Generated by Django 2.1.7 on 2019-04-27 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dayoff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayoff',
            name='approve_status',
            field=models.CharField(choices=[('รอการอนุมัติ', 'รอการอนุมัติ'), ('อนุมัติ', 'อนุมัติ'), ('ไม่อนุมัติ', 'ไม่อนุมัติ')], default='รอการอนุมัติ', max_length=12),
        ),
        migrations.AlterField(
            model_name='dayoff',
            name='type',
            field=models.CharField(choices=[('ลากิจ', 'ลากิจ'), ('ลาป่วย', 'ลาป่วย')], default='ลากิจ', max_length=6),
        ),
    ]