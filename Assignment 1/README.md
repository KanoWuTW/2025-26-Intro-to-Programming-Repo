# What Does This Program Do?

Personal budget tracker is a non-persistent application that helps you manage your spending.

With this program, you can:

- Add income and expense transactions.
- Delete translation records.
- View all transaction records.
- View an overall financial summary (total income, total expense, and net balance).
- View summaries categorized by income or expense type.

# How to Use This Program?

## Requirements

- Python Version: 3.8 or above.

## Running the Program

1. Save the Python file  (e.g., `budget_tracker.py`).
2. Open a terminal.
3. Change the directory to where the file is.
4. Run the program using the following command:
    
    ```powershell
    python budget_tracker.py
    ```
    
5. Follow the instructions in the menu to add, view, and manage transactions.

# Assumptions and Limitations

- Only positive numeric values are accepted for the transaction amount.
- All data is temporarily stored in memory. Transactions vanish after the program exits.
- Inputs in descriptions and categories are case-sensitive (e.g., Food ≠ food). Please use consistent letters for them.
- Currency is assumed to be GBP**£**.

# Test Plan

- Invalid input test
    
    Enter a negative or non-numeric input (e.g.,`-1`, `abc`) and the program should display an error message: `”Invalid amount. Please enter a positive number”` .
    
- Edge test
    
    Since Python’s float cannot handle numbers larger than about `1e308` , entering an amount of `1e309` should cause an overflow(`inf`) or an unexpected value, and the program should be unable to do calculations on it correctly.
    
- Empty transaction list
    
    Start the program and choose “3. List Transactions” , “5. View Overall Summary“, and “6. View Summary by Category” before adding any transactions. The program should print the message: `“No transactions found."`
    
- Income transactions test
    
    Add one or more income records (option 1) with valid amounts and categories.
    
    Then view “5. View Overall Summary”. The program should display the correct total income, and the net balance should reflect `Income - Expense`.
    
- Delete function test
    
    Add multiple transactions, then select “4. Delete Transaction” and enter a valid index (e.g., `1`). The program should remove the corresponding transaction and print a confirmation message. Also, try entering an index out of range. The program should display `“Invalid index”`.
    
- Category summary check
    
    Add some incomes/expenses with different categories (e.g., `Food`, `Education`, `Salary`). Then choose “6. View Summary by Category”. Each category should display the correct accumulated total for both income and expenses.
    

# Completion Report

## Task 2

In this task, I created a function named `display_menu()` that runs when the program starts. It prints out 7 options for users to choose from, prompting them to enter inputs using the `input()` function and directing them to corresponding sub-functions via if-else statements.

## Task 3

In Task 3, I created a function, `add_transaction(current_transactions, transaction_type)`, that prompts users to create a new transaction record. I used try& except to prevent invalid input. Inside the try scope, `amount = float(input("Enter amount:"))`makes sure `amount` can only be float numbers, and `if amount < 0: raise ValueError()` ensures only positive numbers are accepted.

The user’s input will be stored in a temporary dictionary, `transac`, and this dictionary will be appended to `transactions` list.

Finally, a message with the transaction type and amount is printed out, confirming that the new record has been added successfully.

## Task 4

In this task, I created a function `list_transactions(transactions)` that prints every record in the transactions list. If the list is empty, a message "No transactions found.” will be printed; otherwise, a for loop will iterate through the list and print the transaction type, amount, description, and category for each record with an index.

## Task 5

In Task 5, I defined a function `delete_transaction(transactions)` to remove transactions from the list. This function first checks if the list is empty; if not, it calls `list_transactions(transactions)` to list all transactions and prompts users to select one to delete using an index.

I applied try& except to ensure the user’s input indexes are both positive numbers and within the range of the list.

I used `remove()` to delete the transaction selected by users. Since the first transaction displayed by `list_transactions(transactions)` starts from 1, the indexes entered by the user must be reduced by one. Therefore, the code is like this:

```python
deleteIndex = number_of_Transaction - 1                
transactions.remove(transactions[deleteIndex])
```

## Task 6

In the last task, I wrote three functions: `calculate_summary(transactions)`, `print_overall_summary(summary_data)`, and `print_summary_by_category(transactions)`.

- `calculate_summary(transactions)` first creates a temporary dictionary: `summary_data` to store total income, expense, and net balance. Then a for loop iterates through transactions to calculate and store total expense and income, and when they are done, net balance can be therefore calculated by reduce total income by total expense. Lastly, summary_data is returned by the function.
- `print_overall_summary(summary_data)` takes what returned by `calculate_summary(transactions)`as argument. It prints total expense, total income, and net balance.
- `print_summary_by_category(transactions)` creates two temporary dictionaries: expense and income. Then a for loop iterates through transactions and assign them to their type of dictionary. In each dictionary, keys are the categories and values are the total amounts for each category. Finally, the data of temporary dictionaries is printed out and the function returns.

In the last task, I wrote three functions: `calculate_summary(transactions)`, `print_overall_summary(summary_data)`, and `print_summary_by_category(transactions)`.

- `calculate_summary(transactions)` first creates a temporary dictionary, `summary_data`, to store the total income, expense, and net balance. Then, a for loop iterates through transactions to calculate and store the total expense and income. When this is done, the net balance can be calculated by subtracting the total expense from the total income. Lastly, the function returns summary_data.
- `print_overall_summary(summary_data)` takes what returned by `calculate_summary(transactions)`as argument. It prints total expense, total income, and net balance.
- `print_summary_by_category(transactions)` creates two temporary dictionaries: one for expenses and one for income. Then, a for loop iterates through transactions and assigns them to their corresponding dictionary type. In each dictionary, the keys represent the categories, and the values represent the total amounts for each category. Finally, the data of temporary dictionaries is printed out, and the function returns.

## The missed part: Add Income

Although this assignment does not require students to handle income inputs, I added myself to verify that the program runs correctly, especially in the part involving calculating the net balance. Therefore, my program calls `add_transaction(transactions,"Income")` when the user selects option one:

```python
# Rest part of the code ...
if inp == 1:        # Add Income
    add_transaction(transactions,"Income")
elif inp == 2:      # Add Expenses
    add_transaction(transactions,"Expense")
# Rest part of the code ...
```

Since `add_transaction(current_transactions, transaction_type)` is reusable, I do not have to alter it, and it can handle incomes correctly.