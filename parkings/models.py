from django.db import models

# Create your models here.

class Parkings(models.Model):
	id = models.AutoField(primary_key=True)
	x = models.IntegerField(null=False)
	y = models.IntegerField(null=False)
	isOccupied = models.BooleanField(default=False)

	def __str__(self):
		return "id: {} ({},{}) isOccupied: {}".format(self.id,self.x, self.y,self.isOccupied)