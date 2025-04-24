'''
 70) [CHALLENGE] Create a program that displays the first 10 elements of the Fibonacci Sequence:
     1 1 2 3 5 8 13 21...
'''

fibonacci = [1, 1]

for i in range(2, 10):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

print(f'First 10 elements of the Fibonacci Sequence: {", ".join(map(str, fibonacci))}')

input("Press Enter to Exit ... ")