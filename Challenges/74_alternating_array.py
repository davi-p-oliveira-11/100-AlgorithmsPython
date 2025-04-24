'''
 74) Create a program that automatically fills (using logic, not just direct assignment) 
    a numerical array with 10 positions, as follows:  
   `5 3 5 3 5 3 5 3 5 3`  
   `0 1 2 3 4 5 6 7 8 9`  
'''

arr4 = [5 if i % 2 == 0 else 3 for i in range(10)]

print(arr4)

print(' '.join(map(str, arr4)))

print(' '.join(map(str, range(10))))

input("Press Enter to exit ... ")
