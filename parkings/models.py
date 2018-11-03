from django.db import models

# Create your models here.

class Parkings(models.Model):
	x = models.IntegerField(null=False)
	y = models.IntegerField(null=False)
	isOccupied = models.BooleanField(default=False)

	def __str__(self):
		return "x: {} - y: {} isOccupied: {}".format(self.x, self.y,self.isOccupied)