'''This is my To-Do list Application which is the minimum vaible product
This program allows users to add and manage daily tasks'''

#Initialise the main dictionary which contains all the different tasks and their categories/lists
task_lists = {}

main_menu_options = ["1.Create List", "2.Delete Lists", "3.Open Lists", "4.Save & Exit"]

print("Welcome to To-Do List Application") #welcome statement

#Main menu function for the To-Do list app - displays the options
def main():
    while True:
        print("Main Menu")
        for option in main_menu_options:
                print(option)
        user_main_menu_choice = int(input("Choose an option from (1,2,3,4):" ))
        if user_main_menu_choice == 1:
            print("Menu Option chosen: Create List")
            create_list()
        elif user_main_menu_choice == 2:
            print("Menu Option chosen: Delete Lists ")
            delete_lists()
        elif user_main_menu_choice == 3:
            print("Menu Option chosen: Open List ")
            open_list()
        elif user_main_menu_choice == "4":
            print("Menu Option chosen: Save & Exit ")
            save_exit()
        else:
            print("Your answer was invalid please enter a number from 1,2,3,4 correctly")

def create_list(): #adds a list that the user creates to the main dictionary of the catogries
    print("Create a category/list for your tasks to fall under") 
    name_list = input("Create a name for the list: ")
    
    #Create a new emtpy list inside the dictionary
    task_lists[name_list] = []

    print(f'Your list {name_list} has been created') #tells user that list is acutally created

def delete_lists(): #Deletes a list
    global task_lists
    print("Delete any lists you wouldn't like")
    if len(task_lists) == 0: #if no lists are already in the task lists dictionary.
        print("There no current lists to delete go to menu and create one")
    
    print("Available Lists:")
    for i, category in enumerate(task_lists.keys(), start=1):
        print(f"{i}.{category}")
    list_delete_choice = int(input("Enter the number of the list you want to delete"))
    list_name = list(task_lists.keys())[list_delete_choice - 1] #creates a list of all key values and indexs it with the users choice to get the user choice values
    del task_lists[list_name] # removes the user choice value that was indexed stored by using the varaible above
    print(f'your list, is deleted')
    

'''def open_list(): #Displays a current list/category that already exist in the dictionary  

def save_exit(): #programs closes
     
#My second menu when you choose to open a list, then for example choose to mark tasks complete
def list_menu(): #second menu
    
def add_task(): #add tasks/adds values to an individual catorgy list that was chosen
     
def mark_task_complete(): #marks the tasks complete so when viewing open lists to view tasks it show complete
     
def view_tasks():
     
def return_main_menu(): #goes to main menu'''

main()
     