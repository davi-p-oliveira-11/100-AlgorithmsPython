'''
8) Develop a program that reads a distance in meters and displays the corresponding values in other units.

Example:
Enter a distance in meters: 185.72
The distance of 185.72m corresponds to:
0.18572Km
1.8572Hm
18.572Dam
1857.2dm
18572.0cm
185720.0mm
'''

meters = float(input("Enter a distance in meters: "))

kilometers =  meters / 1000
hectometers = meters / 100
decameters =  meters / 10
decimeters =  meters * 10
centimeters = meters * 100
milimeters =  meters * 1000

print(f'''
    The distance of {meters}m is equal to: \n {kilometers}Km \n {hectometers}Hm \n {decameters}Dam \n {decimeters}dm \n {centimeters}cm \n {milimeters}mm
''')

input("Press enter to exit ... ")