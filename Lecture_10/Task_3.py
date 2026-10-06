names = ["Laptop", "Phone", "Headphones", "Monitor"]
prices = [1200, 800, 150, 300]
ratings = [4.8, 4.5, 4.2, 4.9]

products = list(zip(names, prices, ratings))
print("product: ", products, "\n")

sorted_products_by_price = sorted(products, key=lambda x: x[1], reverse=True)
print("sorted products by price: ", sorted_products_by_price, "\n")

sorted_products_by_rating = sorted(products, key=lambda x: x[2], reverse=True)
print("sorted products by rating: ", sorted_products_by_rating, "\n")