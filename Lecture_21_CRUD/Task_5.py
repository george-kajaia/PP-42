import requests
from requests.exceptions import HTTPError

base_url = 'https://crudcrud.com/api/f4e6dc31c0d94d6ab30e0e01db80a041'
timeout = 5

id = '6ae864f814936103e8ff2b9e'

try:
    response = requests.delete(f"{base_url}/product/{id}", timeout=timeout)
    response.raise_for_status()
    print(f"Product deleted successfully")   
except HTTPError as e:
    print(e)