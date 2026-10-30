from dataclasses import dataclass
import json

@dataclass
class Product:
    name: str
    price: int
    in_stock : bool

p1 = Product("First Product", 10, True)
p2 = Product("Second Product", 20, True)
p3 = Product("Third Product", 30, True)

print(f"Product Data: Name={p1.name}; price={p1.price}; in_stock ={p1.in_stock}")
print(f"Product Data: Name={p2.name}; price={p2.price}; in_stock ={p2.in_stock}")
print(f"Product Data: Name={p3.name}; price={p3.price}; in_stock ={p3.in_stock}")
