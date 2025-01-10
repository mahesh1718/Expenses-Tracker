import re
import csv
import reactions
import tabulate
from datetime import date

def main():
    file()


def expensetype():
    while True:
        s = input("Type of expense (e.g., Medical, Rental, School or College fee, anything else): ").lower()
        if not re.match(r"^[a-zA-Z\s]+$", s):
                print("Expense type should not contain numbers or symbols. Please try again.")
                continue
        return s


def expenditure(Type):
    types = ["medical", "rental", "school fee", "college fee", "other"]
    if Type in types:
        s = int(input("Spent amount: "))
        if Type == "medical":
            print(f"Is everything ok? {reactions.sad()}")
            confirmation = input("Yes / No: ").lower()
            if confirmation == "yes":
                print(f"Be healthy and keep yourself happy {reactions.happy()}")
            else:
                print(f"Don't worry, everything will be okay {reactions.winking()}")
        elif Type == "rental":
            print(f"Done for this month {reactions.congo()}")
        elif Type in ["school fee", "college fee"]:
            print(f"Study and keep yourself motivated in every moment {reactions.happy()}")
        return s


def get_budget():
    try:
        with open("budget.txt", "r") as file:
            content = file.read().strip()
            if content == "":  # If the file is empty
                raise ValueError("Budget file is empty.")
            return int(content)  # Try to convert the content to an integer
    except (FileNotFoundError, ValueError) as e:
        print(f"Error reading the budget: {e}. Please enter a new budget.")
        return None  # Return None to prompt the user for a new budget


def set_budget(budget):
    with open("budget.txt", "w") as file:
        file.write(str(budget))  # Write the budget to the file


def budget():
    # Check if there is a saved budget
    saved_budget = get_budget()

    if saved_budget is not None:
        # Ask if the user wants to use the saved budget or set a new one
        use_saved = input(f"Your left over budget is {saved_budget}. Do you want to use it? (yes/no): ").lower()
        if use_saved == 'yes':
            return saved_budget
        else:
            # If the user doesn't want to use the saved budget, ask for a new one
            new_budget = int(input("Enter your budget for this month: "))
            set_budget(new_budget)  # Save the new budget to the file
            return new_budget
    else:
        # If no saved budget exists, prompt the user to set a new budget
        new_budget = int(input("Enter your budget for this month: "))
        set_budget(new_budget)  # Save the new budget to the file
        return new_budget


def saving(Budget, Paid):
    return Budget - Paid


def Date():
    return date.today()


def spenton():
    while True:
        s = input("On which have you spent the money (e.g., Medicines, etc.): ")
        try:
            if s.isdigit():
                raise ValueError("Expense type should not be a number.")
            return s
        except ValueError as e:
            print(e)


def file():
    while True:
        k = input("Type 'done' to exit the entering format then it will display your list: ").lower()
        if k == "done":
            return formating()

        Budget = budget()  # Get the budget
        Type = expensetype()  # Get the expense type
        Spent_on = spenton()  # Get what the money was spent on
        Paid = expenditure(Type)  # Get the amount paid
        Remaining = saving(Budget, Paid)  # Calculate remaining budget

        # Update the budget file with the new remaining budget
        set_budget(Remaining)

        Today = Date()

        with open("Expenses.csv", "a", newline="") as file:
            fieldnames = ["Date(YYYY-MM-DD)", "Type of expense", "Spent on", "Paid", "Budget", "Total remaining in this month"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            file.seek(0, 2)
            if file.tell() == 0:
                writer.writeheader()

            writer.writerow({
                "Date(YYYY-MM-DD)": Today,
                "Type of expense": Type,
                "Spent on": Spent_on,
                "Paid": Paid,
                "Budget": Budget,
                "Total remaining in this month": Remaining
            })
        print("Expense recorded successfully!")
        print(f"you saved {Remaining} {reactions.fire()}")


def formating():
    # Read and display the CSV content
    with open("Expenses.csv", "r") as table:
        reader = csv.DictReader(table)
        rows = list(reader)
        if rows:
            print(tabulate.tabulate(rows, headers="keys", tablefmt="grid"))
        else:
            print("No data available in the table.")


if __name__ == "__main__":
    main()
