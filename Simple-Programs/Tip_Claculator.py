print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
percentage_tip = input("What percentage tip would you like to give? 10, 12, 0r 15? $")
people_splitting =  input("How many people are splitting the bill? ")
tip = (float(total_bill) * (int(percentage_tip)/100))
total_bill_including_tip = float(total_bill) + tip
each_person_pays = total_bill_including_tip / int(people_splitting)
# final_amount = round(each_person_pays, 2)
final_amount = "{:.2f}".format(each_person_pays)
print(f"Each person should pay: ${final_amount}")
