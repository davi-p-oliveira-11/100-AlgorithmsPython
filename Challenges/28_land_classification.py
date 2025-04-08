"""
28) Write a program that asks the user to input the width and length of a 
rectangular plot of land. The program should then calculate and display the 
area of the land in square meters. 
Additionally, the program should classify the
land based on the following criteria:

Less than 100 square meters: POPULAR
Between 100 and 500 square meters: MASTER
Greater than 500 square meters: VIP
"""

width = float(input("Enter the width of the land: "))
length = float(input("Enter the length of the land: "))

area = width * length

if area < 100:
    print(f"The land measures {area:.1f} square meters, so it is a Popular Land.")
elif 100 <= area <= 500:
    print(f"The land measures {area:.1f} square meters, so it is a Master Land.")
else:
    print(f"The land measures {area:.1f} square meters, so it is a VIP Land.")

input("Press Enter to exit... ")
