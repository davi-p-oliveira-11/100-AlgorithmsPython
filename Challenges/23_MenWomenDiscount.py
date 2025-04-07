'''
23) In an exclusive promotion for Women's Day, 
a store wants to give discounts to everyone, 
but especially to women. 
Create a program that reads the customer's name, gender, 
and the purchase value and calculates the price with a discount. Knowing that:   

Men get a 5% discount
Women get a 13% discount 

'''

customer_name = input("Type your name: ")
customer_gender = input("Enter your gender F for female and M male:").upper()
purchase_amount = float(input("What was the total value of the purchase ? "))

men_discount = purchase_amount * 0.05
women_discount = purchase_amount * 0.13

complete_value_men = purchase_amount - men_discount
complete_value_women = purchase_amount - women_discount

if customer_gender == 'F':
  print(f'''{customer_name} made a purchase of {purchase_amount:.2f} USD
             and earned a discount of 13% and will pay {complete_value_women} USD
        ''')
elif customer_gender == 'M':
  print(f'''
            {customer_name} made a purchase of {purchase_amount:.2f} USD
            and earned a discount of 5% and will pay {complete_value_men} USD
        ''')
else:
  print("Enter a valid gender, F for female M for male !")


input("Press Enter to Exit ... ")