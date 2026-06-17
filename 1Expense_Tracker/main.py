# connectivity using modules and files
from tracker import Tracker
from pathlib import Path



# filepaths and extra variables
BASE_DIR = Path(__file__).parent
json_path = BASE_DIR/"expenses.json"





# initializing user
try:
    name = (input("Enter the username (if user does not exist in the database, new user will be created) :\n> ").strip().lower())
    if name == "":
        name = "defaultuser"
    user = Tracker(name)
    good = True
except Exception as e:
    print(f"Initialization error : {e}")
    good = False


# methods for the Tracker class
methods = {
    "add" : user.add_expense,
    "show" : user.show_expenses,
    "total" : user.total_expense,
    "delete" : user.delete_expense,
    "search" : user.search_category,
    "category" : user.category_total,
    "stats" : user.expense_stats,
    "top" : user.top_category,
    "monthlyexpense" : user.monthly_expense
}
usages = {
    "add" : "to enter an expense in the database\n<add amount_number category_name>",
    "show" : "to show all the expenses with their category\n<show>",
    "total" : "to show the total expense done\n<total>",
    "delete" : "to delete an expense using the 'show' command\n<delete expense_number>",
    "search" : "to show the expenses using a particular category\n<search category_name>",
    "category" : "to get the total expense of a particular category\n<category category_name>",
    "stats" : "to get the statistic report of the expenses\n<stats>",
    "top" : "to get the top 3 category on which expenses are the most\n<top>",
    "monthlyexpense" : "to get the total expense done in the recent month\n<monthlyexpense>"
}


# user interaction
print("====Welcome====")
print("--Enter 'help' for seeing all the commands--")
print("--Enter 'usage' for seeing the syntax of commands--")
while good:
    command = input("> ").strip().lower()
    parts = command.split()
    if not parts:
        continue
    method = parts[0]
    arg_list = parts[1:]
    print()

    if method == "help":
        for methodd in methods:
            print(methodd)
        print()
        continue
    elif method == "usage":
        for usage in usages:
            print(f"{usage} : {usages[usage]}\n")
        print()
        continue
    elif method == "exit":
        print("====Take Care!====")
        break
    if method not in methods:
        print("--Entered commmand in not recognised, enter 'help' or 'usage' for more information--")
        print()
        continue


    
    try:
        if method not in methods:
            print("--Entered command is not registered--")
        else:
            methods[method](*arg_list) #unpacking list and passing in the function
    except Exception as e:
        print("--Usage : <func> <arg1> <arg2>--")



    # func = getattr(user, "methodname")
    # func() -> runs the function
    print()


else:
    print("--Unable to proceed due to some internal error--")