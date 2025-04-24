'''
  72) Create a program that automatically fills a numerical array with 8 positions, as follows:
     999 999 999 999 999 999 999 999
      0   1   2   3   4   5   6   7
'''
arr2 = [(i + 1) * 5 for i in range(10)]

print(arr2) 

print(' '.join(map(str, arr2)))

print(' '.join(map(str, range(10))))

input("Press Enter to exit ... ")
