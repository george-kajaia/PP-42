import requests
from requests.exceptions import HTTPError

base_url = 'https://crudcrud.com/api/f4e6dc31c0d94d6ab30e0e01db80a041'
timeout = 5

id = '6ae8bdacf7265c03e85cbf74'

try:
    response = requests.get(f"{base_url}/product/{id}", timeout=timeout)
    print(response.status_code)
    if response.status_code == 200:
        response = requests.delete(f"{base_url}/product/{id}", timeout=timeout)
        response.raise_for_status()
        print(f"Product deleted successfully")
    else:
        print(f"Product with Id={id} not found")
except HTTPError as e:
    print(e)