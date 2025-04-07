'''
25) [CHALLENGE] Create a program that reads the lengths of three line segments.
Analyze their lengths and determine whether it is possible to form a triangle with these segments.
Mathematically, for three segments to form a triangle, the length of each side must be less than the sum of the other two.
'''

side_1 = float(int("Enter the length of the first side: "))
side_2 = float(int("Enter the length of the second side: "))
side_3 = float(int("Enter the length of the third side: "))

if side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_2 + side_3 > side_1:
  print("The given segments can form a triangle. ")
else:
  print("The given segments cannot form a triangle. ")

input("Press Enter to Exit ... ")