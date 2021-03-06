# Generated by Django 4.0.2 on 2022-02-24 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bios', '0002_bioinfo_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='bioinfo',
            name='skill',
            field=models.CharField(choices=[('predictive', 'Predictive Modeling'), ('machinelearning', 'Machine Learning'), ('deeplearning', 'Deep Learning'), ('nlp', 'Natural Language Processing'), ('recommendation', 'Recommendation System'), ('ltv', 'LTV'), ('optimization', 'Optimization'), ('mmm', 'Markov Chain'), ('measurement', 'Measurement'), ('abtest', 'ABTesting')], default='default', max_length=300),
            preserve_default=False,
        ),
    ]
