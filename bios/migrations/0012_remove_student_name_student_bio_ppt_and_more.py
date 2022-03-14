# Generated by Django 4.0.3 on 2022-03-09 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bios', '0011_student_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.AddField(
            model_name='student',
            name='bio_ppt',
            field=models.ImageField(blank=True, null=True, upload_to='bio_ppt/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]