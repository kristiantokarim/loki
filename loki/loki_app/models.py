from django.db import models

# Create your models here.


class MockEntry(models.Model):
	end_point = models.TextField()
	request = models.TextField()
	response = models.TextField()
