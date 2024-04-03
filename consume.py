import requests

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjAyMjEwMzMzIiwibmFtZSI6IkNoYWlydWwgSW1hbSBJJ3phYXoiLCJpYXQiOjEyMDIyMTAzMzN9.wYNImonVfSREQbgkX6ir72SQlW_0cbZW-7U-bY0KMhg"
headers = {'Authorization': f'Bearer {token}'}

response = requests.get('http://localhost:5000/api/data', headers=headers)
print(response.json())

response = requests.get('http://localhost:5000/api/data/1', headers=headers)
print(response.json())

response = requests.get('http://localhost:5000/REGION/ACEH', headers=headers)
print(response.json())

response = requests.get('http://localhost:5000/1997', headers=headers)
print(response.json())
