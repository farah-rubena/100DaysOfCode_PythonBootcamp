print("Welcome to Tip Calculator!!!")
total_bill = float(input("Enter the total bill: $"))
tip_percentage = int(input("Whta percentage tip wpuld you like to give 10, 12 or 15: "))
total_persons = int(input("How many people to spilt the bill?: "))

bill_with_tip = (tip_percentage / 100 * total_bill) + total_bill

bill_per_person = bill_with_tip / total_persons

print("Each person should pay: $ {:.2f}".format(bill_per_person))
