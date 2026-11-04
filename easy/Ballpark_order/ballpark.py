order = input("Enter Your Order: ")
total_price_raw = 0

order_list = order.split()

for i in order_list:
  if i.lower() == "nachos":
    total_price_raw += 6.00

  elif i.lower() == "pizza":
    total_price_raw += 6.00

  elif i.lower() == "cheeseburger":
    total_price_raw += 10.00

  elif i.lower() == "water":
    total_price_raw += 4.00

  else:
    total_price_raw += 5.00

print(f"Total Price: ${total_price_raw:.2f}")
