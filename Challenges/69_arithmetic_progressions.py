'''
   69) [CHALLENGE] Develop a program that reads the first term and the common difference of an 
      arithmetic progression (AP), displaying the first 10 elements of the AP and the sum of all 
      values in the sequence.
'''

first_term = float(input('Enter the first term of the AP: ') or '0')
common_difference = float(input('Enter the common difference: ') or '0')

ap_sequence = []
sum_ap = 0

for i in range(10):
    term = first_term + i * common_difference
    ap_sequence.append(term)
    sum_ap += term

print(f'First 10 elements of the AP: {", ".join(map(str, ap_sequence))}')
print(f'Sum of all values in the sequence: {sum_ap}')


input("Press Enter to Exit ... ")