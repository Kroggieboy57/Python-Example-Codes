unit=input("Enter the unit:")
unit=unit.lower()
base=float(input(f"Enter base of the triangle (in {unit})"))
height=float(input(f"Enter the height of the triangle (in {unit})"))
area=0.5*base*height
print(area)