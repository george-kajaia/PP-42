class Cart:
    cart = ["apple", "cheese", "bread", "milk"]

    @staticmethod
    def get_items():
        print(f"Items are: {Cart.cart}")

    @staticmethod
    def append_new_item(item):
        Cart.cart.append(item)
        print(F"A new item was added: {item}")

    @staticmethod
    def get_last_item():
        return Cart.cart.pop()


Cart.get_items()
Cart.append_new_item("Butter")
print(f"The last added item is: {Cart.get_last_item()}")