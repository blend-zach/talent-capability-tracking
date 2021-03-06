# Generated by Django 4.0.2 on 2022-03-01 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bios', '0004_bioinfo_client_bioinfo_industry'),
    ]

    operations = [
        migrations.AddField(
            model_name='bioinfo',
            name='email',
            field=models.CharField(default='abc@gmail.com', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bioinfo',
            name='technique',
            field=models.CharField(choices=[('Python', 'Python'), ('SQL', 'SQL'), ('Spark', 'Spark'), ('GCP', 'GCP'), ('AWS', 'AWS'), ('Databricks', 'Databricks'), ('R', 'R'), ('Snowflakes', 'Snowflakes'), ('Java', 'Java'), ('C/C++', 'C/C++')], default='python', max_length=300),
            preserve_default=False,
        ),
    ]
