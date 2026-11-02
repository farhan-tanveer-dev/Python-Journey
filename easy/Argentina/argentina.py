try:
  
  price_dollors = int(input("Dollors Price : "))
  price_pesos = int(input("Pesos Price : "))
  
  # 2 cents = 1 Pesos
  # 1 cents = 1/2 Pesos
  # 100 cents = 50 Pesos
  c_dollors = price_dollors * 50
  
  if price_pesos>c_dollors:
    print("Dollors")
  elif price_pesos<c_dollors:
    print("Pesos")
  elif price_pesos==c_dollors:
    print("You can use Either Pesos or Dollors")
    
except:
  print("Enter Valid Prices")
  