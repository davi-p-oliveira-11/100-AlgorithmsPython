"""
30) [CHALLENGE] Redo algorithm 25, adding the feature to display the type of triangle that will be formed:

EQUILATERAL: all sides are equal
ISOSCELES: two sides are equal
SCALENE: all sides are different
"""

side_1 = float(input("Enter the length of the first side: "))
side_2 = float(input("Enter the length of the second side: "))
side_3 = float(input("Enter the length of the third side: "))

if side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_2 + side_3 > side_1:
    print("The given segments can form a triangle.")

    if side_1 == side_2 and side_2 == side_3:
        print("Equilateral (All sides are equal).")
    elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
        print("Isosceles (Two sides are equal).")
    else:
        print("Scalene (All sides are different).")
else:
    print("The given segments cannot form a triangle.")

input("Press Enter to Exit ... ")
