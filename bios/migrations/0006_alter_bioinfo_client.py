# Generated by Django 4.0.3 on 2022-03-07 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bios', '0005_bioinfo_email_bioinfo_technique'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bioinfo',
            name='client',
            field=models.CharField(max_length=300),
        ),
    ]
