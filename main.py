print("Welcome to Daily Expense Tracker!")

expenses = []

number = int(input("How many expenses do you want to enter? "))

for i in range(number):

    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))

    expenses.append(amount)

    print("Added successfully!")

total = sum(expenses)

print("\n----- Expense Summary -----")

print("Total expenses:", total)

print("Thank you for using Expense Tracker!")