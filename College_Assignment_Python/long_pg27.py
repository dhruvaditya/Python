class Product:

    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, number_of_items):
        discount = 0
        if number_of_items < 10:
            pass
        elif 10 <= number_of_items < 99:
            discount = 10
        else:
            discount = 20
        price = (100 - discount) / 100 * self.price
        return price * number_of_items

    def make_purchase(self, quantity):
        self.amount -= quantity


name = input('name:')
amount = int(input('Digit amount of items'))
price = int(input('Digit price of items'))

# name, amount, price = 'shoes', 200, 33

shoes = Product(name, amount, price)
quantity = int(input('Digit amount of items to buy'))


print(f'cost for {quantity} {shoes.name} = {shoes.get_price(quantity)}')
shoes.make_purchase(quantity)
print(f'remaining stock: {shoes.amount}\n')

#cost for 4 shoes = 132.0
# remaining stock: 196
#
# cost for 12 shoes = 356.4
# remaining stock: 184
#
# cost for 112 shoes = 2956.8
# remaining stock: 72

