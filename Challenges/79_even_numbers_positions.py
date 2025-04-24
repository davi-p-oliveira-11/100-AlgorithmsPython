'''
   79) Develop a program that reads 10 integers and stores them in an array. 
       At the end, display which even numbers were entered and the positions 
       where they are stored.
'''

numbers2 = []
even_numbers = []
even_indexes = []

i = 0
while i < 10:
    try:
        input_value = input(f"Enter integer {i + 1}: ")
        num = int(input_value)
        numbers2.append(num)
        if num % 2 == 0:
            even_numbers.append(num)
            even_indexes.append(i)
        i += 1
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

print("Numbers entered:", ', '.join(map(str, numbers2)))
print("Even numbers:", ', '.join(map(str, even_numbers)))
print("Positions of even numbers:", ', '.join(map(str, even_indexes)))


input("Press Enter to exit ... ")