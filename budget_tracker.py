
# -----------------------------------------Task 2-----------------------------------------

# Create a list to store all transactions
transactions = [] 

def display_menu():
    # Display the main menu and let the user select a function.
    # The user can add income/expenses and print transaction details.
    # Select 7 (Exit) to terminate the program.

    # Args:
    #     None
    # Returns:
    #     None

    exit = False
    
    # Keep looping until the user exits the program.
    while exit == False:    
        print("\n--- Personal Budget Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. List Transactions")
        print("4. Delete Transaction")
        print("5. View Overall Summary")
        print("6. View Summary by Category")
        print("7. Exit")

        # This loop ensures that only valid selections are accepted.
        while True:         
            try:
                # Prompt the user to select an option.
                inp = int(input("\nPlease enter your choice:"))     
                if inp > 7 or inp < 1:
                    raise ValueError()
                break
            except:
                # Show an error message.
                print("Accept only options 1~7.")                   
  
        if inp == 1:        # Add Income
            pass
        elif inp == 2:      # Add Expenses
            add_transaction(transactions,"Expense")
        elif inp == 3:      # List Transactions
            list_transactions(transactions)
        elif inp == 4:      # Delete Transaction
            delete_transaction(transactions)
        elif inp == 5:      # View Overall Summary
            print_overall_summary(calculate_summary(transactions))
        elif inp == 6:      # View Summary by Category
            print_summary_by_category(transactions)
        elif inp == 7:      # Exit
            exit = True

    # Termination message
    print("\nThanks for using :D")  
    return


#-----------------------------------------Task 3-----------------------------------------

def add_transaction(current_transactions, transaction_type):
    # Add a transaction to the transactions list.

    # Args:
    #     current_transactions (transactions)
    #     transaction_type ("Income" or "Expense")
    # Returns:
    #     None

    # Handle income transactions.
    if transaction_type == "Income":
        pass
        
    # Handle expense transactions.
    elif transaction_type == "Expense":
        # Ensure only positive numbers are accepted.
        # Return early if an invalid value is entered.
        try:
            # Prompt the user to enter an amount.
            amount = float(input("Enter amount:"))
            if amount < 0:
                raise ValueError()
        except:
            # Print an error message and return.
            print("Invalid amount. Please enter a positive number.")
            return

        # Prompt the user to enter a description and category
        description = input("Enter description:")
        category = input("Enter category:")

        # Create a temporary transaction record.
        transac = {
            "type": transaction_type,
            "amount": amount,
            "description": description,
            "category": category
        }
        current_transactions.append(transac)

    return

#-----------------------------------------Task 4-----------------------------------------

def list_transactions(transactions):
    # List all transaction records in transactions list.

    # Args:
    #     transactions(transactions)
    # Returns:
    #     None

    # If there are no transactions, print a message instead.
    if len(transactions) == 0:                 
        print("No transactions found.")
    else:
        print("\n--- All Transactions ---")
        # Print all transactions.
        for i in range(len(transactions)):      
            print(f"{i+1}. [{transactions[i]["type"]}] -  £{transactions[i]["amount"]} - {transactions[i]["description"]} (Category: {transactions[i]["category"]})")
    
    return

#-----------------------------------------Task 5-----------------------------------------

def delete_transaction(transactions):
    # Prompt the user to delete a transaction.

    # Args:
    #     transactions(transactions)
    # Returns:
    #     None

    # Return if there are no transactions.
    if len(transactions) == 0:          
        return
    
    # List all transaction records.
    list_transactions(transactions)     
    
    # Ask the user which transaction to delete.
    # Create an index for the record to be deleted.
    dele = 0

    # Ensure that only a valid index is accepted.
    try:    
        dele = int(input("Which of the following transactions would you like to delete?"))
        if dele < 1 or dele> len(transactions):
            raise ValueError()
    except:
        print("Invalid index.")
        return                        
        
    # Decreases index by one so the correct record can be deleted
    deleteIndex = dele-1                
    
    transactions.remove(transactions[deleteIndex])
    
    # Deletion successful message
    print(f"No.{dele} transaction has been deleted")

    return 


#-----------------------------------------Task 6-----------------------------------------

def calculate_summary(transactions):
    # Return a dictionary containing the total income, total expense, and net balance.
    
    # Args:
    #     transactions(transactions)
    # Returns:
    #     summary_data
    

    # Initialises the dictionary to be returned
    summary_data = {
        "Income": 0,
        "Expense": 0,
        "Net Balance": 0
    }

    # Calculates the total expense and income and store them in summary_data
    for i in transactions:
        if i["type"] == "Expense":
            summary_data["Expense"] = summary_data["Expense"] + i["amount"]
        elif i["type"] == "Income":
            summary_data["Income"] = summary_data["Income"] + i["amount"]
    
    # Net Balance = Total Income - Total Expense
    summary_data["Net Balance"] = round(summary_data["Income"] - summary_data["Expense"],2)

    return summary_data


def print_overall_summary(summary_data):
    # Print the data in summary_data.
    
    # Args:
    #     summary_data, possibly from calculate_summary(transactions)
    # Returns:
    #     None

    # Prints overall summary
    print("\n--- Overall Summary ---")
    for key, values in summary_data.items():
        print(f"{key}: £{values}")
    
    print("-----------------------")

    return


def print_summary_by_category(transactions):
    # Calculate the total income and expense for each category.
    # Print the results.

    # Args:
    #     transactions(transactions)
    # Returns:
    #     None

    # Creates a temporary dictionary for results
    expense = {}    
    income = {}
    for i in transactions:
       # Store the amount in the expense dictionary.
       if i.get("type") == "Expense":
           # If the category does not exist, create it.
           if expense.get(i["category"]) == None:
               expense[i["category"]] = 0
           # Accumulate the total for this category.
           expense[i["category"]] = expense[i["category"]] + i.get("amount")

       # Store the amount in the income dictionary.
       elif i.get("type") == "Income":
           # If the category does not exist, create it.
           if income.get(i["category"]) == None:
               income[i["category"]] = 0
           # Accumulate the total for this category.
           income[i["category"]] = income[i["category"]] + i.get("amount")

    # Print the expense summary.
    print("\n--- Expenses by Category ---")
    for key, value in expense.items():
        print(f"{key}: £{value}")

    # Print the income summary.
    print("\n--- Income by Category ---")
    for key, value in income.items():
        print(f"{key}: £{value}")

    print("----------------------------")

    return

# -----------------------------------------Testing Data-----------------------------------

Ex1 = {
    "type": "Expense",
    "amount": 12.61,
    "description": "Amazon books: C++ Primer",
    "category": "Education"
}

Ex2 = {
    "type": "Expense",
    "amount": 2500.99,
    "description": "tution",
    "category": "Education"
}

Ex3 = {
    "type": "Expense",
    "amount": 1.69,
    "description": "Drinks",
    "category": "Food"
}

Ex4 = {
    "type": "Expense",
    "amount": 10.16,
    "description": "lunch",
    "category": "Food"
}

Ex5 = {
    "type": "Expense",
    "amount": 2,
    "description": "Shampo",
    "category": "Groceries"
}

Ex6 = {
    "type": "Expense",
    "amount": 8,
    "description": "O2 mobile",
    "category": "Network"
}

Ic1 = {
    "type": "Income",
    "amount": 1500,
    "description": "Oct salary",
    "category": "Salary"
}

Ic2 = {
    "type": "Income",
    "amount": 35.4,
    "description": "Amazon",
    "category": "Refund"
}

Ic3 = {
    "type": "Income",
    "amount": 500,
    "description": "Rent",
    "category": "Other"
}


transactions.append(Ex1)
transactions.append(Ex2)
transactions.append(Ex3)
transactions.append(Ex4)
transactions.append(Ex5)
transactions.append(Ex6)

transactions.append(Ic1)
transactions.append(Ic2)
transactions.append(Ic3)
#----------------------------------------------------------------------------------------

display_menu()