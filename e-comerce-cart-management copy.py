#Shopping cart program

products=[]
prices=[]
total=0


while True:
    product=input("Enter the product name to buy (q to quit): ")
    if product.lower()== "q":
        break
    else:
        price=float(input(f"Enter the price of the product {product}:"))
        products.append(product)
        prices.append(price)

print("-----YOUR CART-----")

for product in products:
    print(product)

for price in prices:
    total +=price

print()

print(f"Your total is:{total}")

