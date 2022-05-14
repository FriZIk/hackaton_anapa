from curses import meta
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from drf_extra_fields.fields import Base64ImageField
from .models import Marker
import re
# from rosambros.settings import model
from PIL import Image
import numpy as np
import zipfile
import json
from io import BytesIO
import base64

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
      pass
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

def deflatten(names):
  names.sort(key=lambda name:len(name.split('/')))
  deflattened = []
  while len(names) > 0:
    name = names[0]
    if name[-1] == '/':
      subnames = [subname[len(name):] for subname in names if subname.startswith(name) and subname != name]
      for subname in subnames:
        names.remove(name+subname)
      deflattened.append((name, deflatten(subnames)))
    else:
      deflattened.append(name)
    names.remove(name)
  return deflattened

class MarkersArchiveSerializer(serializers.Serializer):
  file = serializers.FileField()

  def create(self, validated_data):
    file = validated_data.pop('file')

    if file.name.split('.')[-1] != 'zip':
      error = {'message': 'You need to send .ZIP archive'}
      raise serializers.ValidationError(error)

    try:
      with zipfile.ZipFile(file, 'r') as zip_file:
        namelist = deflatten(zip_file.namelist())
        _root_dir = namelist[0][1]
        _root_dir_name = namelist[0][0] # ...

        photos_dir_names_list = _root_dir[1][1]
        photos_dir_name = _root_dir[1][0] # .

        metadata_dir_names_list = _root_dir[0][1]
        metadata_dir_name = _root_dir[0][0] # .
        
        markers = []

        for i in range(0, len(photos_dir_names_list)):
          # photo
          photo_name = photos_dir_names_list[i]
          photo_file_path = _root_dir_name + photos_dir_name + photo_name
          photo_content = zip_file.read(photo_file_path)
          dataEnc = BytesIO(photo_content)
          img = Image.open(dataEnc)
          img = img.convert("RGB")
          buffered = BytesIO()
          img.save(buffered, format="JPEG")
          img_str = base64.b64encode(buffered.getvalue())

          # metadata
          metadata_name = metadata_dir_names_list[i]
          metadata_file_path = _root_dir_name + metadata_dir_name + metadata_name
          metadata_content = zip_file.read(metadata_file_path)
          marker_jsn = json.loads(metadata_content)

          marker = {
            'image': img_str.decode('utf-8'),
            'gps': marker_jsn['gps'],
            'marker_type': marker_jsn['marker_type'],
            'address': marker_jsn['address'],
            'created_on': marker_jsn['created_on'],
          }

          markers.append(marker)
        
        serializer = MarkerSerializer(data=markers, many=True)
        if serializer.is_valid():
          serializer.save()
          # return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, statua=status.HTTP_400_BAD_REQUEST)

      return file
    except Exception as e:
      return e

    return file