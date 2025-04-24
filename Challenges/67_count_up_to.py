'''
  67) Create a program using the "for" loop that reads a positive integer and displays a count 
     from 0 to the entered value.

     Enter a number: 9  
     Count: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, END !
'''

entered_number = int(input('Enter a positive number: '))

for counter in range(0, entered_number + 1):
    print(counter)

print('END !')


input("Press Enter to exit ... ")