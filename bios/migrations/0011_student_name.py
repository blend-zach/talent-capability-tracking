# Generated by Django 4.0.3 on 2022-03-09 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bios', '0010_remove_student_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(default='name_place', max_length=100),
            preserve_default=False,
        ),
    ]
