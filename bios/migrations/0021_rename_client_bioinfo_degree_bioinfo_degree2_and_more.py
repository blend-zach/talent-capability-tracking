# Generated by Django 4.0.2 on 2022-04-21 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bios', '0020_alter_student_bio_ppt_alter_student_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bioinfo',
            old_name='client',
            new_name='degree',
        ),
        migrations.AddField(
            model_name='bioinfo',
            name='degree2',
            field=models.CharField(default='N/A', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bioinfo',
            name='degree3',
            field=models.CharField(default='N/A', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bioinfo',
            name='major2',
            field=models.CharField(default='N/A', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bioinfo',
            name='major3',
            field=models.CharField(default='N/A', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bioinfo',
            name='university2',
            field=models.CharField(default='N/A', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bioinfo',
            name='university3',
            field=models.CharField(default='N/A', max_length=300),
            preserve_default=False,
        ),
    ]
