def calculate_area(bal: str)->int:
  height_a , width_a = map(int , bal.split(","))
  area = height_a*width_a
  return area

bal_a_measures = input("Balcoie A :")
bal_b_measures = input("Balcoie b :")

area_a = calculate_area(bal_a_measures)
area_b = calculate_area(bal_b_measures)

if area_a>area_b:
  print("Apertment A")
if area_b>area_a:
  print("Apertment B")