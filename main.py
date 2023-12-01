# Initialize budget dictionary
budget = {
    "income": 0,
    "expenses": 0,
    "balance": 0,
}

# Function to handle user input for operation
def get_operation():
    operation = input("Which operation do you want to perform? (deposit/withdraw/balance): ")
    if operation == "balance":
        view_budget()
    if operation not in ("deposit", "withdraw","balance"): 
        print(f"Invalid operation '{operation}'. Please try again.")
        return None
    
    return operation

# Function to add income to budget
def add_income(amount):
    budget["income"] += amount
    budget["balance"] += amount
    print(f"Successfully added {amount} to your income.")
    print(f"Your balance is now: {budget['balance']}")

# Function to add expense to budget
def add_expense(amount):
    budget["expenses"] += amount
    budget["balance"] -= amount
    print(f"Successfully added {amount} to your expenses.")
    print(f"Your balance is now: {budget['balance']}")

# Function to display budget
def view_budget():
    print("**Budget Overview**")
    print(f"Income: {budget['income']}")
    print(f"Expenses: {budget['expenses']}")
    print(f"Balance: {budget['balance']}")

# Main program loop
while True:
    operation = get_operation()
    if not operation:
        continue

    # if operation == "balance":
    #     view_budget()

    

    if operation == "deposit":
        amount = float(input(f"How much do you want to {operation}? "))
        add_income(amount)
    elif operation == "withdraw":
        amount = float(input(f"How much do you want to {operation}? "))
        add_expense(amount)
    elif operation == "balance":
        view_budget()
   

    if operation in ("balance"):
        answer = input("Do you want to perform another transaction? (yes/no): ")
    else:
        answer = input("Would you like to perform another operation? (yes/no): ")

    if answer.lower() not in ("yes", "y"):
        break

print("Thank you for using the expense tracker!")


# budget = {'income': 0, 'expenses': 0, 'balance': 0}


# operation = input("which operation do you want to perform? ")

# #Income func
# def add_income(amount):
#     budget['income'] += amount
#     budget['balance'] += amount


# #Expense func
# def add_expense(amount):
#     budget['expenses'] += amount
#     budget['balance'] -= amount


# #Balance func
# def view_budget():
#     print('Income:', budget['income'])
#     print('Expenses:', budget['expenses'])
#     print('Balance:', budget['balance'])


# if operation == 'deposit':
#     amount = int(input("How much are you depositing: "))
#     add_income(amount)
#     print(f"Your balance is: {budget['balance']}")
#     answer = input("would like to perform another transaction? ")
#     if answer == 'yes':
#         operation = input("which operation do you want to perform? ")
#         if operation == 'deposit':
#             amount = int(input("How much are you depositing? "))
#             add_income(amount)
#             print(f"Your balance is: {budget['balance']}")
#             answer = input("would like to perform another transaction? ")

#         elif operation == 'withdraw':
#             amount = int(input("How much are you withdrawing? "))
#             add_expense(amount)
#             print(f"Your balance is: {budget['balance']}")
#             answer = input("would like to perform another transaction? ")
#     else:
#         print("Goodbye!")

# elif operation == 'withdraw':
#     amount = int(input("How much are you withdrawing? "))
#     add_expense(amount)
#     print(f"Your balance is: {budget['balance']}")
#     if answer == 'yes':
#         operation = input("which operation do you want to perform? ")
#         if operation == 'deposit':
#             amount = int(input("How much are you depositing? "))
#             add_income(amount)
#             print(f"Your balance is: {budget['balance']}")

#         elif operation == 'withdraw':
#             amount = int(input("How much are you withdrawing? "))
#             add_expense(amount)
#             print(f"Your balance is: {budget['balance']}")
#     else:
#         print("Goodbye!")

# else:
#     print(f"invalide operation {operation}, you can only perform {budget['income']} and {budget['expenses']}")

