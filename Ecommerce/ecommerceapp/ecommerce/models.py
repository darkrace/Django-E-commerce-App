# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date
from django.db import models

# Create your models here.
class Registration(models.Model):
	Name = models.CharField(max_length=200)
	Password = models.CharField(max_length=200)

class Product(models.Model):
    Name = models.ForeignKey('Registration')
    Prod = models.ForeignKey('PProduct')
	
class PProduct(models.Model):
    PName = models.CharField(max_length=200)
    Price = models.CharField(max_length=200)
    Item = models.CharField(max_length=200)
    Image = models.FileField()
	