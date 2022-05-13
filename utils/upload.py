import requests
import config
import base64

class ClientJWT:
  def __init__(self, base_url, req_url, username, password):
    self.base_url = base_url
    self.req_url = req_url
    self._username = username
    self._password = password
    self._session = requests.Session()
    self._headers = {
      'User-Agent': 'Mozilla/5.0'
    }
  
  def auth_jwt_create(self):
    payload = {
      "username": self._username,
      "password": self._password,
    }

    response = self._session.post(self.base_url + "/auth/jwt/create", headers=self._headers, json=payload)
    response.raise_for_status()

    self._refresh = response.json()['refresh']
    self._access = response.json()['access']
  
  def upload_marker(self, image_path, marker_type, gps, address):
    self.auth_jwt_create()

    payload = {
      "image": base64.b64encode(open(image_path, "rb").read()).decode("utf-8"),
      "marker_type": marker_type,
      "gps": gps,
      "address": address,
    }

    response = self._session.post(self.base_url + self.req_url, headers=self._headers, json=payload)
    response.raise_for_status()

    print(response.json())

client_jwt = ClientJWT(config.base_url, config.req_url, config.credentials['username'], config.credentials['password'])
client_jwt.upload_marker("/home/h1w/Dev/hackathon/hackaton_anapa/utils/photo_2020-10-14_02-10-32.jpg", 1, "45.434, 38.678", "pizda")
