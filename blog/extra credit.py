import json
import requests

response = requests.get(...)
json_data = json.loads(response.text)
