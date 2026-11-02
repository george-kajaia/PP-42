import requests
from requests.exceptions import HTTPError

base_url = 'https://crudcrud.com/api/f4e6dc31c0d94d6ab30e0e01db80a041'

timeout = 5

product = {
    "name": "Gaming Laptop",
    "price": 6000,
    "in_stock": False}

try:
    response = requests.post(f"{base_url}/product", json=product, timeout=timeout)
    response.raise_for_status()
    print(f"Product added successfully: {response.json()}")   
except HTTPError as e:
    print(e)