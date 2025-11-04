




# Task 2

transactions = []

test1 = {
    "type": "Expense",
    "amount": 100.2,
    "description": "gas",
    "category": "daily"
}

test2 = {
    "type": "Expense",
    "amount": 200.35,
    "description": "tution",
    "category": "education"
}

test3 = {
    "type": "Expense",
    "amount": 10,
    "description": "drinks",
    "category": "food"
}

test4 = {
    "type": "Expense",
    "amount": 110,
    "description": "lunch",
    "category": "food"
}

test5 = {
    "type": "Expense",
    "amount": 5,
    "description": "shampo",
    "category": "daily"
}

transactions.append(test1)
transactions.append(test2)
transactions.append(test3)
transactions.append(test4)
transactions.append(test5)

def display_menu():
    option_1 = "1. Add Income"
    option_2 = "2. Add Expense"
    option_3 = "3. List Transactions"
    option_4 = "4. Delete Transaction"
    option_5 = "5. View Overall Summary"
    option_6 = "6. View Summary by Category"
    option_7 = "7. Exit"

    exit = False
    while exit == False:
        print("\n--- Personal Budget Tracker ---")
        print(option_1)
        print(option_2)
        print(option_3)
        print(option_4)
        print(option_5)
        print(option_6)
        print(option_7)

        while True:
            try:
                inp = int(input("Please enter your choice:"))
                if inp > 7 or inp < 1:
                    raise ValueError()
                break
            except:
                print("Take 1~ 7 only")
                
        
        if inp == 2:
            add_transaction(transactions,"Expense")
        elif inp == 3:
            list_transactions(transactions)
        elif inp == 4:
            delete_transaction(transactions)
        elif inp == 5:
            print_overall_summary(calculate_summary(transactions))
        elif inp == 6:
            print_summary_by_category(transactions)
        elif inp == 7:
            exit = True

    return


# Task 3

def add_transaction(current_transactions, transaction_type):
    if transaction_type == "Income":
        print("1515151")
    elif transaction_type == "Expense":
        while True:
            try:
                amount = float(input("Enter amount:"))
                if amount < 0:
                    raise ValueError()
                break
            except:
                print("Invalid amount. Please enter a positive number.")
                return

        description = input("Enter description:")
        category = input("Enter category:")

        transac = {
            "type": transaction_type,
            "amount": amount,
            "description": description,
            "category": category
        }
        transactions.append(transac)

    return

# Task 4

def list_transactions(transactions):
    if len(transactions) == 0:
        print("No transactions found.")
    else:
        print("\n--- All Transactions ---")
        for i in range(len(transactions)):
            print(f"{i+1}. [{transactions[i]["type"]}] -  £{transactions[i]["amount"]} - {transactions[i]["description"]} (Category: {transactions[i]["category"]})")
    
    return

# Task 5

def delete_transaction(transactions):
    if len(transactions) == 0:
        return
    
    list_transactions(transactions)
    
    dele = 0
    while True:
        try:
            dele = int(input("Which of the following transactions would you like to delete?"))
            if dele < 1 or dele> len(transactions):
                raise ValueError()
            break
        except:
            print("Invalid index.")
            return
    
    deleteIndex = dele-1
    transactions.remove(transactions[deleteIndex])

    print(f"No.{dele} transaction has been deleted")

    return 


# Task 6

def calculate_summary(transactions):
    summary_data = {
        "Income": 0,
        "Expense": 0,
        "Net Balance": 0
    }

    for i in transactions:
        if i["type"] == "Expense":
            summary_data["Expense"] = summary_data["Expense"] + i["amount"]
        elif i["type"] == "Income":
            summary_data["Income"] = summary_data["Income"] + i["amount"]
    summary_data["Net Balance"] = summary_data["Income"] - summary_data["Expense"]

    return summary_data


def print_overall_summary(summary_data):
    print("\n--- Overall Summary ---")
    for key, values in summary_data.items():
        print(f"{key}: £{values}")
    
    print("-----------------------")
    return

def print_summary_by_category(transactions):
    
    print("\n--- Expenses by Category ---")

    dic = {}
    for i in transactions:
        dic[i["category"]]
        dic[i["category"]] = dic[i["category"]] + i["amount"]
    

    print("----------------------------")

    return

    
    
    


display_menu()
