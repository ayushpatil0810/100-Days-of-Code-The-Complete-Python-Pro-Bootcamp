#Day 2
print("Welcome to the the tip calculator !")
bill = float(input("What was the total bill ? $ "))
tip = int(input("How much  % tip would you like to give ? "))
split = int(input("How many people to split the bill ? "))

final_amount = round(((bill + ((tip/100) * bill)) / split), 2)

print(f"Each person should pay: ${final_amount}")
