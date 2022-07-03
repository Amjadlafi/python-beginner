print("welcome to TIP Calculate")
bill  = float(input("what was the total bill $?"))
tip = int(input("How much tip would you like gave you? 5 , 10 .15"))
people = int(input("How many people  to the spilt the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_personal = total_bill/ people
final_amount = round(bill_per_personal , 2)
final_amount = "{:.2f}".format(bill_per_personal)
print(f" Each person should pay: ${final_amount}")
