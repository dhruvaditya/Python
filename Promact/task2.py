class Product:
    #Product Class
    def __init__(self, name, price, quantity, item_type):
        self.name = name
        #strip is used to seperate integer and string
        self.price = float(price.strip(' RS'))
        self.quantity = int(quantity)
        self.product_type = item_type
#Dunder method used to represent the data in more user friendly way
    def __str__(self):
        return f"{self.name}, {self.price} RS, {self.quantity}, {self.product_type}"

class Invertory:
    # instance method to initializes a newly created object
    def __init__(self, products):
        self.products = products
#this will return the length of the total_products present in the list
    def total_products(self):
        return len(self.products)
#append is used to add product
    def add_product(self, product):
        self.products.append(product)
#For loop to iterate through all the products
    def print_all_products(self):
        for product in self.products:
            print(product)
#Calculating length of the list after the addition of the product
    def total_products_after_addition(self):
        return len(self.products)

    def filter_by_type(self, product_type):
        return [product for product in self.products if product.product_type == product_type]

    def remove_product(self, product_name):
        self.products = [product for product in self.products if product.name != product_name]

    def quantity_after_purchase(self, product_name, quantity_purchased):
        for product in self.products:
            if product.name == product_name:
                product.quantity -= quantity_purchased
                return product.quantity
        return 0
#Here we are calculating the total_cost by iterating through two loops and the cost is added to the variable and returned after round after 2 decimal place
    def calculate_total_cost(self, purchases):
        total_cost = 0
        for purchase in purchases:
            product_name, quantity = purchase
            for product in self.products:
                if product.name == product_name:
                    total_cost += product.price * quantity
                    break
        return round(total_cost, 2)

# Input: List of products
products_input = [
    "lettuce, 10.5 RS, 50, Leafy green",
    "cabbage, 20 RS, 100, Cruciferous",
    "pumpkin, 30 RS, 30, Marrow",
    "cauliflower, 10 RS, 25, Cruciferous",
    "zucchini, 20.5 RS, 50, Marrow",
    "yam, 30 RS, 50, Root",
    "spinach, 10 RS, 100, Leafy green",
    "broccoli, 20.2 RS, 75, Cruciferous",
    "garlic, 30 RS, 20, Leafy green",
    "silverbeet, 10 RS, 50, Marrow"
]

# Create Product objects from input
products = [Product(*product.split(', ')) for product in products_input]

# Create InventorySystem object
inventory = Invertory(products)

# Print total number of products
print("Total Number of Products:", inventory.total_products())

# Add a new product (Potato, 10RS, 50, Root)
inventory.add_product(Product("Potato", "10 RS", 50, "Root"))

# Print the list of all products and total number of products
print("\nList of All Products:")
inventory.print_all_products()
print("Total Number of Products:", inventory.total_products_after_addition())

# Print all products of type Leafy green
print("\nLeafy Green Products:")
leafy_green_products = inventory.filter_by_type("Leafy green")
for product in leafy_green_products:
    print(product)

# Remove Garlic from the list
inventory.remove_product("garlic")

# Print the total number of products remaining
print("\nTotal Number of Products after Removing Garlic:", inventory.total_products())

# Purchase quantities and print the final quantity of cabbage
cabbage_quantity_after_purchase = inventory.quantity_after_purchase("cabbage", 50)
print("\nFinal Quantity of Cabbage in Inventory:", cabbage_quantity_after_purchase)

# Calculate the total cost for the purchases
purchases = [("lettuce", 1), ("zucchini", 2), ("broccoli", 1)]
total_cost = inventory.calculate_total_cost(purchases)
print("\nTotal Cost for Purchases:", total_cost, "RS")
