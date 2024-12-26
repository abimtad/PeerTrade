from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Category(models.Model):
	name = models.CharField(max_length=50)

	class Meta:
		ordering = ('name',)
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name


class Item(models.Model):
	category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
	name = models.CharField(max_length=30)
	price = models.FloatField()
	description = models.TextField(blank=True, null=True)
	image = models.ImageField(upload_to='items_image', blank=True, null=True)
	is_sold = models.BooleanField(default=False)
	owner = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return  self.name

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.image.path)

		output_size = (200, 200)

		img = img.resize(output_size, Image.Resampling.LANCZOS)

		img.save(self.image.path)