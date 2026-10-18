
from datetime import datetime

# Spreadsheet Automation Menu - Week 2
menu_options = ["Input Data", "View Current Data", "Generate Report"]

print("Raywag8025 Spreadsheet Automation Menu")
print("Choose a number from the following options")

# Each option represents one available action in the menu.
for number, option in enumerate(menu_options, start=1):
    print(f"{number} {option}")

# The next line retrieves the inputted option and stores into the variable called selection.
selection = input("Enter your selection: ")

if selection in ("1", "2", "3"):
    print(f"You selected {selection} at {datetime.now()}")
else:
    print("Error: Invalid choice selected.")
