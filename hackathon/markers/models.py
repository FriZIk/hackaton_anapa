from django.db import models
from django.dispatch import receiver
import os
from PIL import Image
from django.core.files import File
from io import BytesIO
from django.core.files.base import ContentFile

# поврежднение дороги
# знак
# разметка

STATUS = (
  (0, "Draft"),
  (1, "Publish"),
)

MARKER_TYPE = (
  (0, "Road Damage"),
  (1, "Road Sign"),
  (2, "Road Markings"),
)

class Marker(models.Model):
  image = models.ImageField(upload_to='uploads/', blank=True, null=True)
  marker_type = models.IntegerField(choices=MARKER_TYPE, default=0)
  gps = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  created_on = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ('-created_on',)
  
  def __str__(self):
    return f'{self.id}'
  
  def save(self, *args, **kwargs):
    if self.image:
      filename = '{}.jpg'.format(self.image.name.split('.')[0].lstrip('uploads/'))

      image = Image.open(self.image)
      # For PNG images discarding the alpha channel and fill it with some color
      if image.mode in ('RGBA', 'LA'):
        background = Image.new(image.mode[:-1], image.size, '#fff')
        background.paste(image, image.split()[-1])
        image = background
      image_io = BytesIO()
      image.save(image_io, format='JPEG', quality=100)

      # change the image field value to be the newly modified image value
      self.image.save(filename, ContentFile(image_io.getvalue()), save=False)
    super(Marker, self).save(*args, **kwargs)