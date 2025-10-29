print("Welcome to the smart currency converter! (Dollar to Sum)")

travel_budget = int(input("Enter your travel budget in USD: "))
dollar_exchange = int(input("Enter the dollar exchange rate: "))
unexpected_percent = float(input("Enter the percentage for unexpected expenses: "))
travelers = int(input("Enter number of travelers: "))

total_budget = travel_budget * dollar_exchange
percent = total_budget * (unexpected_percent / 100)
all_budget = total_budget + percent
every_traveler = all_budget / travelers

print("Calculation results:")

print(f"Total budget: {total_budget} sum")
print(f"Unforeseen expenses: {percent} sum")
print(f"Available budget: {all_budget} sum")
print(f"From every traveler: {every_traveler} sum")
