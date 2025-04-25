expences=[]
def add_expense():
    name=input("Enter the name of the expense: ")
    amount=float(input("Enter the amount of the expense: "))
    expences.append({"name": name, "amount": amount})
    print(f"Expense '{name}' of amount {amount} added successfully .")

def view_expenses():
    print("Expenses:")
    for expense in expences:
        print(f"Name: {expense['name']}, Amount: {expense['amount']}")
        print()

def total_expenses():
    total = sum(expense['amount'] for expense in expences)
    print(f"Total expenses: {total}")   

while True:
    print("Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        total_expenses()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
    print()
    print("Thank you for using the expense tracker!")
    print("Goodbye!")

         