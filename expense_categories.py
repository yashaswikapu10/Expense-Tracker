categories = ['Food', 'Transportation', 'Entertainment', 'Other']

def get_category():
    print("Select category:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    choice = int(input("Enter choice: "))
    return categories[choice - 1]