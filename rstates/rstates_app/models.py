from django.db import models

# Create your models here.


class Package (models.Model):
	product_number = models.CharField(max_length=20,primary_key=True)
	product_name = models.CharField(max_length=50,null=True)
	package_name = models.CharField(max_length=50,null=True)
	ee327r = models.CharField(max_length=50,null=True)
	ee327d = models.CharField(max_length=50,null=True)
	ee403r = models.CharField(max_length=50,null=True)
	ee403d = models.CharField(max_length=50,null=True)
	ee404r = models.CharField(max_length=50,null=True)
	ee404d = models.CharField(max_length=50,null=True)
	es1406r = models.CharField(max_length=50,null=True)
	es1406d = models.CharField(max_length=50,null=True)
	es1407r = models.CharField(max_length=50,null=True)
	es1407d = models.CharField(max_length=50,null=True)
	es1408r = models.CharField(max_length=50,null=True)
	es1408d = models.CharField(max_length=50,null=True)
	es1409r = models.CharField(max_length=50,null=True)

	def __unicode__(self):
		return self.product_number + " - " + self.product_name + " - " + self.package_name