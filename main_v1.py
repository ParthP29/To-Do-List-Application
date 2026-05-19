'''This is my To-Do list Application which is the minimum vaible product
This program allows users to add and manage daily tasks'''

#Initialise the main dictionary which contains all the different tasks and their categories/lists
task_lists = {}

main_menu_options = ["1.Create List", "2.Delete Lists", "3.Open Lists", "4.Save & Exit"]

#Main menu function for the To-Do list app - displays the options
def main():
    print("Main Menu")
    for option in main_menu_options:
            print(option)
    user_main_menu_choice = int(input("Choose an option from (1,2,3,4):" ))
    if user_main_menu_choice == 1:
        print("Menu Option chosen: Create List")
    elif user_main_menu_choice == "2":
        print("Menu Option chosen: Delete Lists ")
    elif user_main_menu_choice == "3":
        print("Menu Option chosen: Open List ")
    elif user_main_menu_choice == "4":
        print("Menu Option chosen: Save & Exit ")
    else:
        print("Your answer was invalid please enter a number from 1,2,3,4 correctly")

def create_list(): #adds a list that the user creates to the main dictionary of the catogries

def delete_lists(): #Deletes a list

def open_list(): #Displays a current list/category that already exist in the dictionary  

def save_exit(): #programs closes