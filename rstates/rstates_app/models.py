from django.db import models

# Create your models here.


class Package (models.Model):
	product_number = models.CharField(max_length=20)
	product_name = models.CharField(max_length=50)
	package_name = models.CharField(max_length=50)
	ee327r = models.CharField(max_length=50)
	ee327d = models.CharField(max_length=50)
	ee403r = models.CharField(max_length=50)
	ee403d = models.CharField(max_length=50)
	ee404r = models.CharField(max_length=50)
	ee404d = models.CharField(max_length=50)
	es1406r = models.CharField(max_length=50)
	es1406d = models.CharField(max_length=50)
	es1407r = models.CharField(max_length=50)
	es1407d = models.CharField(max_length=50)
	es1408r = models.CharField(max_length=50)
	es1408d = models.CharField(max_length=50)
	es1409r = models.CharField(max_length=50)

	def __unicode__(self):
		return self.product_number + " - " + self.product_name + " - " + self.package_name

