import data_storage
import expense_categories
import data_analysis
import error_handling

def main():
    print("Welcome to the Expense Tracker")
    while True:
        try:
            print("1. Add Expense")
            print("2. View Summary")
            print("3. Exit")
            choice = int(input("Enter choice: "))
            if choice == 1:
                amount = float(input("Enter amount: "))
                description = input("Enter description: ")
                category = expense_categories.get_category()
                data_storage.add_expense(amount, description, category)
            elif choice == 2:
                data_analysis.display_summary()
            elif choice == 3:
                break
            else:
                print("Invalid choice. Try again.")
        except ValueError as e:
            error_handling.handle_value_error(e)

if _name_ == "_main_":
    main()