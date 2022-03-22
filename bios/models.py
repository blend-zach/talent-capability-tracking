from pyexpat import model
from django.db import models
from django import forms
import os
# Create your models here.
def path_and_rename(instance, filename):
    upload_to = 'images/'
    ext = filename.split('.')[-1]
    print(instance.name)
    filename = '{}.{}'.format(instance.name, ext)
    return os.path.join(upload_to, filename)

def path_and_rename2(instance, filename):
    upload_to = 'bio_ppt/'
    ext = filename.split('.')[-1]
    print(instance.name)
    filename = '{}.{}'.format(instance.name, ext)
    print(filename)
    return os.path.join(upload_to, filename)

class Student(models.Model):
    photo = models.ImageField(null=True, blank=True, upload_to=path_and_rename)
    bio_ppt = models.FileField(upload_to=path_and_rename2)
    name = models.CharField(max_length=100)


class BioInfo(models.Model):
    LOCATION_CHOICES = [
        ('Columbia, MD (HQ)', 'Columbia, MD (HQ)'),
        ('New York, NY', 'New York, NY'),
        ('Denver, CO', 'Denver, CO'),
        ('India', 'India'),
        ('Remote', 'Remote')
    ]

    SKILL_CHOICES = [
        ('Predictive Modeling', 'Predictive Modeling'),
        ('Machine Learning', "Machine Learning"),
        ('Deep Learning', "Deep Learning"),
        ('Natural Language Processing', 'Natural Language Processing'), 
        ('Recommendation System', "Recommendation System"),
        ('LTV', 'LTV'),
        ('Optimization', 'Optimization'),
        ('Markov Chain', 'Markov Chain'),
        ('Measurement', 'Measurement'),
        ('AB Testing', 'AB Testing'), 
        ('Business Intelligence', 'Business Intelligence'),
        ('Campaign Design / Execution', 'Campaign Design / Execution'), 
        ('Cloud Services', 'Cloud Services'),
        ('Customer Segmentation and Insights', 'Customer Segmentation and Insights'),
        ('Data Governence', 'Data Governence'),
        ('Data Visualization', 'Data Visualization'),
        ('Data Wrangling', 'Data Wrangling'),
        ('Data / Network Security', 'Data / Network Security'),
        ('Deployment', 'Deployment'),
        ('Digital Analytics', 'Digital Analytics'),
        ('Personalization', 'Personalization'),
        ('SEO', 'SEO'),
        ('Simulation', 'Simulation'),
        ('Time Series Analysis', 'Time Series Analysis'),
    ]

    INDUSTRIES_CHOICES = [
        ('Retail', 'Retail'),
        ('Grocery', "Grocery"),
        ('Financial Services', "Financial Services"),
        ('Transportation', 'Transportation'), 
        ('Healthcare', "Healthcare"),
        ('B2B', 'B2B'),
        ('Construction', 'Construction'),
        ('Manufacturing', 'Manufacturing'),
        ('Utilities', 'Utilities'),
        ('Insurance', 'Insurance'),
        ('Communication Services', 'Communication Services'),
        ('E Commerce', 'E Commerce'),
        ('Educational Services', 'Educational Services'),
        ('Energy', 'Energy'),
        ('Hospitality', 'Hospitality'),
        ('Information Technology', 'Information Technology'),
        ('Life Sciences', 'Life Sciences'),
        ('Real Estate', 'Real Estate'),
        ('Technology', 'Technology'),
    ]

    CLIENT_CHOICES = [
        ('AARP', 'AARP'),
        ('Acorns', "Acorns"),
        ('CVS', "CVS"),
        ('Grammarly', 'Grammarly'), 
        ('HGV', "HGV"),
        ('Marriott MTA', 'Marriott MTA'),
        ('Sunovion', 'Sunovion'),
        ('Visa', 'Visa'),
        ('Walmart', 'Walmart')
    ]

    TECHNICUQE_CHOICES = [
        ('Python', 'Python'),
        ('SQL', "SQL"),
        ('Spark', "Spark"),
        ('GCP', 'GCP'), 
        ('AWS', "AWS"),
        ('Databricks', 'Databricks'),
        ('R', 'R'),
        ('Snowflakes', 'Snowflakes'),
        ('Java', 'Java'),
        ('C/C++', 'C/C++')
    ]

    POSITION_CHOICES = [
        ('Associate Data Scientist/Intern', 'Associate Data Scientist/Intern'),
        ('Associate Data Scientist, All-Star', 'Associate Data Scientist, All-Star'),
        ('Lead Data Scientist', 'Lead Data Scientist'),
        ('Senior Manager, Data Science', 'Senior Manager, Data Science'),
        ('Director, Data Science', 'Director, Data Science'),
        ('Senior Data Scientist', 'Senior Data Scientist'),
        ('Data Scientist', 'Associate Director, Data Science'),
        ('Manager, Data Science', 'Manager, Data Science '),
        ('Senior Director, Data Science', 'Senior Director, Data Science'),
        ('Marketing Scientist, All-Star', 'Marketing Scientist, All-Star'),
        ('Senior Marketing Scientist', 'Senior Marketing Scientist'),
        ('Associate Marketing Scientist, All-Star', 'Associate Marketing Scientist, All-Star'),
        ('VP, Data Science', 'VP, Data Science'),
        ('SVP, Data Science', 'SVP, Data Science')
    ]

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    position = models.CharField(max_length=100, choices=POSITION_CHOICES, default=None)
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES, default=None)
    skill = models.CharField(max_length=300, choices=SKILL_CHOICES, default=None)
    technique = models.CharField(max_length=300, choices=TECHNICUQE_CHOICES, default=None)
    industry = models.CharField(max_length=300, choices=INDUSTRIES_CHOICES, default=None)
    client = models.CharField(max_length=300)
    intro = models.TextField()
    photo = models.ImageField(null=True, blank=True, upload_to="images/")
    bio_ppt = models.ImageField(null=True, blank=True)

    
    def __str__(self):
        return self.name
    


