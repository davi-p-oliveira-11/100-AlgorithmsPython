'''
  47) Develop an application that displays the result of the 
      expression 500 + 450 + 400 + 350 + 300 + ... + 50 + 0
'''

sum_3 = 0
counter = 500

while counter != 0:
  sum_3 += counter
  counter -= 50


print(f"The sum between 500 + 450 + 400 + 350 + 300 ... + 50 + 0 is: {sum_3}")

input("Press Enter to exit ... ")