from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from .models import Marker
import re
# from rosambros.settings import model
from PIL import Image
import numpy as np

# def validate_single(_img):
#     # img = keras_image.load_img(img_path, target_size=(200,200))
#     # x = keras_image.img_to_array(img)
#     img = Image.open(_img)
#     img.resize((200,200))
#     x = np.array(img)
#     x = np.expand_dims(x, axis=0)
#     images = np.vstack([x])
#     classes = model.predict(images, batch_size=10)
#     result = False
#     if classes[0] < 0.5:
#         # Ambrosia
#         print('Ambrosia')
#         result = True
#     else:
#         # Not ambrosia
#         print('Not ambrosia')
#         result = False
#     return result

class MarkerSerializer(serializers.ModelSerializer):
  image = Base64ImageField()
  class Meta:
    model = Marker
    fields = (
      'id',
      'marker_type',
      'gps',
      'address',
      'image',
      'created_on',
    )
  def create(self, validated_data):
    image = validated_data.pop('image')
    gps = validated_data.pop('gps')
    marker_type = validated_data.pop('marker_type')

    # check gps is valid
    pattern = '^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$'
    match_result = re.match(pattern, gps)

    if match_result:
      print('OK')
    else:
      error = { 'message': 'Validation error. Your data: {} is invalid.'.format(gps) }
      raise serializers.ValidationError(error)

    try:
      address = validated_data.pop('address')
    except Exception as e:
      pass
    
    try:
      marker = Marker.objects.create(gps=gps, image=image, marker_type=marker_type, address=address)
      return marker
    except Exception as e:
      error = {'message': ",".join(e.args) if len(e.args) > 0 else 'Unknown Error'}
      raise serializers.ValidationError(error)