# The below script will ask for 3 inputs. Each input will be based
# on the price of the items - the price is determined by you. The output
# should print the total of the 3 inputs rounded to 2 decimal places e.g
#
#   1 coffee @ $ 2.00
#   1 sandwich @ $ 4.99
#   1 cake @ $ 2.75
#
#   Your total bill is $ 9.74

coffee = input('1 coffee @: $ ')
sandwich = input('1 sandwich @: $ ')
cake = input('1 cake @: $ ')

bill_total = float(coffee) + float(sandwich) + float(cake)
bill_total_rounded = round(bill_total, 2)

print('Your total bill is $', bill_total_rounded)
