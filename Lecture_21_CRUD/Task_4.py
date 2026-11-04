import requests
from requests.exceptions import HTTPError

base_url = 'https://crudcrud.com/api/f4e6dc31c0d94d6ab30e0e01db80a041'
timeout = 5

id = '6ae8bdacf7265c03e85cbf74'

updated_data = {
    "name": "Quantum Computer", 
    "price": 3200, 
    "in_stock": True}

try:
    response = requests.get(f"{base_url}/product/{id}", timeout=timeout)
    if response.status_code == 200:
        response = requests.put(f"{base_url}/product/{id}", json=updated_data, timeout=timeout)
        response.raise_for_status()
        print(f"Product updatetd successfully", "\n")

        print(f"New Product's data:")
        response = requests.get(f"{base_url}/product/{id}", timeout=timeout)
        response.raise_for_status()
        product = response.json()
        print(f"Id: {product['_id']}")
        print(f"Name: {product['name']}")
        print(f"Price: {product['price']}")
        print(f"In Stock: {product['in_stock']}", "\n")
    else:
        print(f"Product with Id={id} not found")
except HTTPError as e:
    print(e)

