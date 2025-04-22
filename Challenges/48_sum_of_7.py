'''
 48) Write a program that reads 7 integer numbers and at the end displays the sum
     between them.
'''

counter = 1
sum_4 = 0

while counter <= 7:
  number = int(input("Type a number: "))
  sum_4 += number
  counter += 1


print(f"The sum of the entered numbers is {sum_4}")


input("Press Enter to Exit ... ")