from dataclasses import dataclass, asdict
import json

@dataclass
class Product:
    name: str
    price: int
    in_stock : bool

p1 = Product("First Product", 10, True)
p2 = Product("Second Product", 20, True)
p3 = Product("Third Product", 30, True)

p1_dict = asdict(p1)
p2_dict = asdict(p2)
p3_dict = asdict(p3)

print("\n")

p1_json = json.dumps(p1_dict, indent=4)
print(p1_json)
p2_json = json.dumps(p2_dict, indent=4)
print(p2_json)
p3_json = json.dumps(p3_dict, indent=4)
print(p3_json)
