loyalty_customer = True
total_bill = 50

if loyalty_customer and total_bill >100:
  total_bill = total_bill - (float(total_bill)/100)*20
  print(f'Total bill is: {float(total_bill)} Thanks for your regular visit')
elif total_bill >100:
  total_bill = total_bill - (float(total_bill)/100)*10
  print(f'Total bill is: {float(total_bill)} Please register with us for more discounts')
else:
  print((f'Total bill is: {float(total_bill)}'))
  print("Sorry, no discount....")
