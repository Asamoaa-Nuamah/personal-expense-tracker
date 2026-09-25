#controlling the program logic

from add_expense import add_expense
from view_expense import view_expences
from total_expense import calc_total_expenses
from categorizing_expense import cat_expenses
from category_total import calc_spending_category
from delete_expense import delete_expense
from edit_expense import edit_expenses

#adding more than one expense (multiple expenses)
continue_adding = "Y"
while continue_adding == "Y" or continue_adding == "y":
    add_expense()
    answer = input("Do you want to add another expense? (Y/N): ") 

    while answer != "Y" and answer != "y" and answer != "N" and answer != "n":   #validating the input
        print("Make a choice please")
        answer = input("Do you want to add another expense? (Y/N): ")

    if answer == "N" or answer =="n":
        continue_adding = "N"



view_expences() #view expense
calc_total_expenses() #calculates total expense
cat_expenses() #categoring / filtering expenses
calc_spending_category()
delete_expense()
edit_expenses()

