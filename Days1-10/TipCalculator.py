bill = float(input("What is the total of the bill?: $"))
percent = int(input("What percent of tip would you like to give? % "))
totalPeople = int(input("How many people are you spliting the bill between?: "))
percent = percent/100
tipAmount = bill * percent
totalBill = bill+tipAmount
billPerPerson = round((totalBill/totalPeople),2)
print(f"Each person should pay ${billPerPerson}")
