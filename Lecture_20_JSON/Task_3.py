from dataclasses import dataclass
import json

@dataclass
class Product:
    name: str
    price: int
    in_stock: bool

data_str = '{"name": "Laptop", "price": 2500, "in_stock": true}'

data_dict = json.loads(data_str)

p = Product(**data_dict)

print(f"Product Data: Name={p.name}; price={p.price}; in_stock ={p.in_stock}")
