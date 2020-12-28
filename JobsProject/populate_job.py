import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','JobsProject.settings')
import django
django.setup()

from JobsApp.models import *
from faker import Faker
import random
fake=Faker()
def phoneGen():
    d=random.randint(7,9)
    num=''+str(d)
    for i in range(9):
        d=random.randint(0,9)
        num=num+str(d)
    return num
def populate(n):
    for i in range(n):
        fdesgn=fake.random_element(elements=('Analyst','Sr Analyst','Manager','Consultant','Sr Manager','Typeist','Associate Consultant'))
        fopen=random.randint(2,9)
        floc=fake.random_element(elements=('SuperCorridor','Banganga','BawarKua','Novelty','Rajendra Nagar','DAVV'))
        fqual=fake.random_element(elements=('M.Tech','M.Com','B.Com','B.E','B.C.A'))
        fexp=str(random.randint(2,8))+'years'
        fcontract='2 years'
        fcontact=phoneGen()
        femail=fake.email()
        indore_rec=IndoreJobs.objects.get_or_create(desgn=fdesgn,openings=fopen,location=floc,qual=fqual,exp=fexp,contract=fcontract,contact=fcontact,email=femail)
n=int(input("Enter number of records you wanna enter : "))
populate(n)
