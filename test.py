import requests

url = 'http://127.0.0.1:8001/uploadfile'
file = {'file': open('10_1.jpg', 'rb')}
resp = requests.post(url=url, files=file) 
print(resp.json())
