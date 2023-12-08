import math
def paint_calc(height, width, cover):
  can=(height * width)/cover
  can=math.ceil(can)
  print(f"You'll need {can} cans of paint.")


test_h = int(input("Height of room: ")) # Height of wall (m)
test_w = int(input("Width of room: ")) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
