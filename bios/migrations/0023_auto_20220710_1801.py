# Generated by Django 3.2.13 on 2022-07-10 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bios', '0022_bioinfo_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='bioinfo',
            name='application',
            field=models.CharField(blank=True, choices=[('Predictive Modeling', 'Predictive Modeling'), ('Machine Learning', 'Machine Learning'), ('Deep Learning', 'Deep Learning'), ('Natural Language Processing', 'Natural Language Processing'), ('Recommendation System', 'Recommendation System'), ('LTV', 'LTV'), ('Optimization', 'Optimization'), ('Markov Chain', 'Markov Chain'), ('Measurement', 'Measurement'), ('AB Testing', 'AB Testing'), ('Business Intelligence', 'Business Intelligence'), ('Campaign Design / Execution', 'Campaign Design / Execution'), ('Cloud Services', 'Cloud Services'), ('Customer Segmentation and Insights', 'Customer Segmentation and Insights'), ('Data Governence', 'Data Governence'), ('Data Visualization', 'Data Visualization'), ('Data Wrangling', 'Data Wrangling'), ('Data / Network Security', 'Data / Network Security'), ('Deployment', 'Deployment'), ('Digital Analytics', 'Digital Analytics'), ('Personalization', 'Personalization'), ('SEO', 'SEO'), ('Simulation', 'Simulation'), ('Time Series Analysis', 'Time Series Analysis')], default=None, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='bioinfo',
            name='ds_skill',
            field=models.CharField(blank=True, choices=[('Python', 'Python'), ('SQL', 'SQL'), ('Spark', 'Spark'), ('GCP', 'GCP'), ('AWS', 'AWS'), ('Databricks', 'Databricks'), ('R', 'R'), ('Snowflakes', 'Snowflakes'), ('Java', 'Java'), ('C/C++', 'C/C++')], default=None, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='bioinfo',
            name='program_skill',
            field=models.CharField(blank=True, choices=[('Predictive Modeling', 'Predictive Modeling'), ('Machine Learning', 'Machine Learning'), ('Deep Learning', 'Deep Learning'), ('Natural Language Processing', 'Natural Language Processing'), ('Recommendation System', 'Recommendation System'), ('LTV', 'LTV'), ('Optimization', 'Optimization'), ('Markov Chain', 'Markov Chain'), ('Measurement', 'Measurement'), ('AB Testing', 'AB Testing'), ('Business Intelligence', 'Business Intelligence'), ('Campaign Design / Execution', 'Campaign Design / Execution'), ('Cloud Services', 'Cloud Services'), ('Customer Segmentation and Insights', 'Customer Segmentation and Insights'), ('Data Governence', 'Data Governence'), ('Data Visualization', 'Data Visualization'), ('Data Wrangling', 'Data Wrangling'), ('Data / Network Security', 'Data / Network Security'), ('Deployment', 'Deployment'), ('Digital Analytics', 'Digital Analytics'), ('Personalization', 'Personalization'), ('SEO', 'SEO'), ('Simulation', 'Simulation'), ('Time Series Analysis', 'Time Series Analysis')], default=None, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='bioinfo',
            name='tech_stack',
            field=models.CharField(blank=True, choices=[('Python', 'Python'), ('SQL', 'SQL'), ('Spark', 'Spark'), ('GCP', 'GCP'), ('AWS', 'AWS'), ('Databricks', 'Databricks'), ('R', 'R'), ('Snowflakes', 'Snowflakes'), ('Java', 'Java'), ('C/C++', 'C/C++')], default=None, max_length=300, null=True),
        ),
    ]