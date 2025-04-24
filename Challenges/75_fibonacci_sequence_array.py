'''
  75) Create a program that automatically fills (using logic, not just direct assignment) 
     a numerical array with 15 positions with the first elements of the Fibonacci sequence:
     1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
     0 1 2 3 4 5 6  7  8  9  10 11  12  13  14  15
'''

arr5 = [1, 1]

for i in range(2, 15):
    arr5.append(arr5[i - 1] + arr5[i - 2])

print(arr5)

print(' '.join(map(str, arr5)))

print(' '.join(map(str, range(15))))

input("Press Enter to exit ... ")
