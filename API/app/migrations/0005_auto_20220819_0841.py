# Generated by Django 4.1 on 2022-08-19 07:41

from django.db import migrations
import csv
import os
from dotenv import load_dotenv
from django.db import transaction
from django.db import IntegrityError
from dotenv import load_dotenv

load_dotenv()

def load(apps, schema_editor):
  
  Physical = apps.get_model('app', 'PhysicalConstant')
  phy = open(os.getenv('phy'))
  reader3 = csv.reader(phy)
  for name, value, unit, uncertainty in reader3:
    try:
      with transaction.atomic():
        record = Physical(name=name.strip(), value=value, unit=unit, uncertainty=uncertainty)
        record.save()
    except IntegrityError:
      record.delete()
      
  phy.close()
  
  


def reverse_load(apps, schema_editor):
  
  Physical = apps.get_model('app', 'PhysicalConstant')
  Physical.objects.all().delete()




class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_physicalconstant'),
    ]

    operations = [
      migrations.RunPython(load, reverse_load),
    ]
