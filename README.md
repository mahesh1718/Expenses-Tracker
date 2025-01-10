Expensive Tracker
--------------------------
#### Video Demo: https://youtu.be/ojTO9Wj4T7w
--------------------------
#### Description:
Overview
Expensive Tracker is a Python-based project designed to help you manage and track your monthly expenses efficiently. This program allows you to record various expense types like medical, rental, school fees, etc., while keeping an updated record of your remaining budget. It provides helpful feedback based on the type of expense and ensures your financial information is saved in an organized format.

Features
Expense Tracking: Record different types of expenses like medical bills, rent, school or college fees, or any other type.
Budget Management: Set a monthly budget and track the remaining amount as you add expenses.
CSV Output: Save your expense details into a CSV file, making it easy to analyze and view later.
Reaction-based Feedback: Get unique messages and reactions based on your expense type. For instance:
Medical expenses trigger a message encouraging health and positivity.
School or college fees come with motivational messages.
Rental expenses confirm your completion for the month.
Tabular Display: View your expense data in a formatted table using the tabulate library.
How to Use
Set Your Budget:

Enter your budget for the month when prompted.
If you’ve used this program before, you’ll have the option to reuse your leftover budget from the previous session or set a new one.
Record Your Expenses:

Enter the type of expense (e.g., medical, rental).
Provide details of what you spent the money on.
Enter the amount spent. The program checks for valid inputs and calculates the remaining balance automatically.
Get Feedback:

After entering an expense, you’ll receive tailored feedback or reactions based on the type of expense. For example, for medical expenses, the program might ask, "Is everything ok?" and encourage you to stay positive.
Save and Exit:

Type "done" to stop entering expenses.
Your expenses will be saved to a CSV file, and you can view them in a neatly formatted table.
Requirements
Python 3.x
Libraries:
reactions: For emoji-based feedback (custom-coded).
tabulate: For displaying expense data in a table format.
csv: To save and manage expense data.
File Details
Expenses.csv: Stores all recorded expenses in a structured format with the following fields:

Date (YYYY-MM-DD)
Type of expense
Spent on
Paid amount
Initial budget
Remaining balance
budget.txt: Saves the leftover budget from the current month for future use.

Example Workflow
Set a budget of $500.
Record a medical expense of $50 for medicines. The program calculates the remaining budget as $450.
Enter "done" to finish. The data is saved, and you can view it in a table format like:
sql
Copy code
+-------------------+------------------+------------+------+---------+-----------------------------+
| Date(YYYY-MM-DD)  | Type of expense | Spent on   | Paid | Budget  | Total remaining in this month |
+-------------------+------------------+------------+------+---------+-----------------------------+
| 2025-01-10        | Medical         | Medicines  |   50 |     500 |                         450 |
+-------------------+------------------+------------+------+---------+-----------------------------+
Key Notes
Input validations ensure no negative or invalid data is recorded.
Friendly messages make the experience engaging.
Budget management helps you track spending habits effectively.
Future Improvements
Add graphical expense analysis.
Introduce categories for automated sorting.
Allow multiple users to track their budgets
