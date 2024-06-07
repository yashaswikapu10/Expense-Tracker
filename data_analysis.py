import data_storage

def display_summary():
    expenses = data_storage.get_expenses()
    if not expenses:
        print("No expenses recorded.")
        return

    total = sum(expense['amount'] for expense in expenses)
    print(f"Total expenses: ${total:.2f}")
    
    category_totals = {}
    for expense in expenses:
        category = expense['category']
        if category in category_totals:
            category_totals[category] += expense['amount']
        else:
            category_totals[category] = expense['amount']
    
    for category, total in category_totals.items():
        print(f"Total in {category}: ${total:.2f}")

