from django.db import models
from datetime import datetime
# Create your models here.


class Element(models.Model):
  atomic_no = models.CharField(max_length=200, default='')
  element = models.CharField(max_length=200, default='')
  symbol = models.CharField(max_length=200, default='')
  atomic_mass = models.CharField(max_length=200, default='')
  neurons = models.CharField(max_length=200, default='')
  protons = models.CharField(max_length=200, default='')
  Electrons = models.CharField(max_length=200, default='')
  period = models.CharField(max_length=200, default='')
  group = models.CharField(max_length=200, default='')
  phase = models.CharField(max_length=200, default='')
  radioactive = models.BooleanField()
  natural = models.BooleanField()
  metal = models.BooleanField()
  Nonmetal = models.BooleanField()
  metalloid = models.BooleanField()
  kind = models.CharField(max_length=200, default='')
  atomic_radius = models.CharField(max_length=200, default='')
  eletro_negativity = models.CharField(max_length=200, default='')
  ionization_Energy = models.CharField(max_length=200, default='')
  Density = models.CharField(max_length=200, default='')
  Melting_point = models.CharField(max_length=200, default='')
  Boiling_point = models.CharField(max_length=200, default='')
  isotopes = models.CharField(max_length=200, default='')
  discoverer = models.CharField(max_length=200, default='')
  year = models.CharField(max_length=200, default='')
  specific_heat = models.CharField(max_length=200, default='')
  shells = models.CharField(max_length=200, default='')
  valence_electron = models.CharField(max_length=200, default='')
  
  def __str__(self):
     return self.element


class ChemicalConstant(models.Model):
  constant = models.CharField(max_length=200)
  symbol = models.CharField(max_length=200)
  value = models.CharField(max_length=200)
  
  def __str__(self):
     return self.constant
  
   
  
   
class Particle(models.Model):
  name = models.CharField(max_length=30)
  kind = models.CharField(max_length=30)
  spin = models.CharField(max_length=100)
  charge = models.CharField(max_length=100)
  mass = models.CharField(max_length=100)
  
  def __str__(self):
     return self.name
  
 

class PhysicalConstant(models.Model):
  name = models.CharField(max_length=100)
  value = models.CharField(max_length=100)
  unit = models.CharField(max_length=30)
  uncertainty = models.CharField(max_length=100)
  
  def __str__(self):
     return self.name
  

  


     
