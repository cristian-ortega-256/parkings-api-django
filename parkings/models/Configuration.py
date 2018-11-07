from django.db import models

class Configuration(models.Model):
	key = models.CharField(primary_key=True,max_length=100)
	value = models.CharField(max_length=500)

	def __str__(self):
		return "{} | {}".format(self.key, self.value)