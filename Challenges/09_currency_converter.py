'''
9) Write an algorithm that reads how much money a person has in their wallet (in BRL) 
and shows how many US dollars they can buy. Consider 1 USD = 3.45 BRL.
'''

avaiable_brl = float(input('How many BRL you have in your pocket ? '))
dollar_value = avaiable_brl / 3.45

print(f'You can buy {dollar_value:.2f} USD')

input("Press enter to exit ... ")