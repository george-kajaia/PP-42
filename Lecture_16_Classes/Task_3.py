class Product:
    shop_name = "MegaShop"
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, quantity):
        self.stock -= quantity
        
        if quantity > 1:
            print(f"{quantity} {self.name} is sold, remained {self.stock}")
        else:
            print(f"{quantity} {self.name}s are sold, remained {self.stock}")
        
leptops = Product("Leptop", 1500, 15)
leptops.sell(7)
leptops.sell(2)