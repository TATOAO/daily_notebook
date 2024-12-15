import requests

url = "http://127.0.0.1:8000/users/me"

payload = {}
headers = {
  'Authorization': 'Bearer alice'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

