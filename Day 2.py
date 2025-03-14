print("Welcome to the tip calculator! ")
Total_bill=float(input("What was the total bill:\n$"))

People= input("How many people to divide by total bill\n")

Payable_amount= int(Total_bill) / int(People)

percent= int(input("Tip you have to Pay: "))


Tip_percentage=(int(percent)/100)

bill_per_person=round((Payable_amount* Tip_percentage),2)


print(f"Each person should pay: ${bill_per_person}")

