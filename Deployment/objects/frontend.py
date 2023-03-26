import json
def print_menu():
  "Print Options to terminal"
  print("Welcome to the Train Management System")
  print("1. View Train Schedules")
  print("2. Find Route")
  print("3. Admin Login")
  print("4. Exit")

def view_train_schedule():
  #Print all Trains in train schedule
  print("Train Schedule: ")
  with open('trainSchedule.json', 'r') as f:
    data = json.load(f)

  print(json.dumps(data, indent = 4))
  pass



def find_route():
  print("Pick a Transit-System")
  pass

def admin_login():
  pass


#Main Loop
while True:
  print_menu()
  user_choice = input("Please enter your choice (1-4): ")

  if user_choice == "1":
    view_train_schedule()
  if user_choice == "2":
    find_route()
  if user_choice == "3":
    admin_login()
  if user_choice == "4":
    print("Thank You for using the Train Admin System. Goodbye!")
    break
  else:
    print("Invalid Choice. Please enter a number between 1 and 4.")
  