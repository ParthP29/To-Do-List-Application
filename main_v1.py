'''This is my To-Do list Application which is the minimum vaible product
This program allows users to add and manage daily tasks'''

#Initialise the main dictionary which contains all the different tasks and their categories/lists
task_lists = {}

options = ["1.Create List", "2.Delete Lists", "3.Open Lists", "4.Save & Exit"]

#Main menu function for the To-Do list app - displays the options
def main():
    print("Main Menu")
    for option in options:
            print(option)
    user_main_menu_choice = int(input("Choose an option from (1,2,3,4):" ))
    if user_main_menu_choice == 1:
        print("Menu Option chosen: Create List")
    if user_main_menu_choice == "2":
        print("Menu Option chosen: Delete Lists ")
    if user_main_menu_choice == "3":
        print("Menu Option chosen: Open List ")
    if user_main_menu_choice == "4":
        print("Menu Option chosen: Save & Exit ")

main()