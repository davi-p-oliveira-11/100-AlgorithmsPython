'''
  73) Create a program that automatically fills (using logic, not just direct assignment) a numerical array with 10 positions, as follows:
     9 8 7 6 5 4 3 2 1 0
     0 1 2 3 4 5 6 7 8 9
'''

arr3 = [i for i in range(9, -1, -1)]

print(arr3)  

print(' '.join(map(str, arr3)))

print(' '.join(map(str, range(10))))

input("Press Enter to exit ...")
