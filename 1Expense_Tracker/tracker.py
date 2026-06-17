# connectivity using modules and files
import json
from pathlib import Path
from datetime import datetime



# filepaths and extra variables
BASE_DIR = Path(__file__).parent
json_path = BASE_DIR/"expenses.json"



# main Tracker class
class Tracker():
    # i can comfortably code using classes and objects now
    def __init__(self, name):
        self.name = name.strip().lower()
        self.database = self.load_create_database(self.name)
        self.data = self.database["users"][self.name]

    def load_create_database(self, name):
        try:
            with open(json_path, 'r') as f:
                record = json.load(f)
                if name not in record["users"]:
                    record["users"][name] = {
                        "expenses" : []
                    }
                    with open(json_path, 'w') as f:
                            json.dump(record, f, indent = 4)
                            print("--New user created--")
        except Exception as e:
            print("--Creating new database and user--")
            with open(json_path, 'w') as f:
                record = {
                    "users" : {
                        name : {
                            "expenses" : []
                        }
                    }
                }
                json.dump(record, f, indent = 4)
        return record
    
    def load_data(self):
        with open(json_path, 'r') as f:
            return json.load(f)

    def save_data(self):
        with open(json_path, 'w') as f:
            json.dump(self.database, f, indent = 4)

    def add_expense(self, amount, category = ""): 
        if not category:
            print("--Category cannot be empty--")
            return
        try:
            amount = float(amount)
        except ValueError:
            print("--amount should be a numerical value--")
            return
        if amount <= 0:
            print("--Amount should be a postive number--")
            return
        self.data["expenses"].append({
            "amount" : amount,
            "category" : category.lower(),
            "date" : f"{datetime.now().date()}"
        })
        self.save_data()

    def show_expenses(self, arg1 = "", arg2 = ""):
        if not self.data["expenses"]:
            print("--No record to show--")
            return
        for num, expense in enumerate(self.data["expenses"], start = 1): # i understand enumerate now
            print(f"{num:02}.  ₹{expense["amount"]}    \t{expense["category"]}")

    def total_expense(self, arg1 = "", arg2 = ""):
        total = 0
        for expense in self.data["expenses"]:
            total += expense["amount"]
        print(f"Total amount :    ₹{total}")
        return total

    def delete_expense(self, index, arg1 = ""):
        try:
            index = int(index)
        except Exception as e:
            print("--expense_number should be a valid integer--")
            return
        if index <= 0 or index > len(self.data["expenses"]):
            print("--Index not available--")
            return
        self.data["expenses"].pop(index-1)
        self.save_data()

    def search_category(self, category = "", arg1 = ""):
        found = False
        for expense in self.data["expenses"]:
            if category.lower() in expense["category"]:
                print(f"₹{expense["amount"]}    \t{expense["category"]}")
                found = True
        if not found:
            print("--no result matched--")

    def category_total(self, category, arg1 = ""):
        category = category.lower()
        total = 0
        for expense in self.data["expenses"]:
            if expense["category"] == category:
                total += expense["amount"]
        print(f"Total  :  ₹{total} ({category})")

    def expense_stats(self, arg1 ="", arg2 = ""):
        total = self.total_expense()
        count = len(self.data["expenses"])
        if count == 0:
            print("--No result found--")
            return
        print(f"Total expenses :  {count} ONLY")
        print(f"Average expense : ₹{total/count}")

    def top_category(self, arg1= "", arg2 = ""):
        record = {}
        for expense in self.data["expenses"]:
            if expense["category"] not in record:
                record[expense["category"]] = expense["amount"]
            else:
                record[expense["category"]] += expense["amount"]
        for i in range(0, 3):
            if not record: break
            maximum = max(record, key = record.get) # to get the key with maximum value in record
            print(f"{i+1}. {maximum} {record[maximum]}")
            del record[maximum] # to not get the same key again and again

    def monthly_expense(self, arg1= "", arg2= ""):
        total = 0
        mapp = {}
        month = str(datetime.now().date())[5:7]
        data = self.load_data()["users"][self.name]["expenses"]
        for expense in data:
            if expense["date"][5:7] == month:
                total += expense["amount"]
                if expense["category"] not in mapp:
                    mapp[expense["category"]] = expense["amount"]
                else:
                    mapp[expense["category"]] += expense["amount"]
        for key, value in mapp.items():
            print(f"{key}: ₹{value}")
        print(f"Total expense for the recent month -{month}- was ₹{total}")






# other helper functions

