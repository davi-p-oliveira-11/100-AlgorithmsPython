'''
 66) Write a program that reads any number and displays its multiplication table using the "for" loop.
     Enter a number: 5  
     5 x 1 = 5  
     5 x 2 = 10  
     5 x 3 = 15  
     ...
'''

number = 5

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


input("Press Enter to exit ... ")