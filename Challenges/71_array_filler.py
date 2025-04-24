'''
   71) Create a program that automatically fills a numerical array with 8 positions, as follows:
     999 999 999 999 999 999 999 999
      0   1   2   3   4   5   6   7
'''

arr = [999] * 8
print(' '.join(map(str, arr)))

print(' '.join(map(str, range(8))))

input("Press Enter to exit ... ")