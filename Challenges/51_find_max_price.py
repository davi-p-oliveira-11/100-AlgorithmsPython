'''
  51) Create an application that reads the price of 8 products. 
      In the end, display on the screen which was the highest 
      and lowest price entered.
'''

counter = 0
highest_price = float('-inf')  
lowest_price = float('inf')    
products_prices = []

while counter < 8:
    product_price = float(input(f"Enter the price of the product {counter + 1}: "))
    products_prices.append(product_price)

    if product_price > highest_price:
        highest_price = product_price

    if product_price < lowest_price:
        lowest_price = product_price

    counter += 1

    

print(f"Prices entered: {products_prices}")
print(f"Highest price: {highest_price}")
print(f"Lowest price: {lowest_price}")


input("Press Enter to exit ... ")
