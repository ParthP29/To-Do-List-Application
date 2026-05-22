'''This is my To-Do list Application which is the minimum vaible product
This program allows users to add and manage daily tasks'''

#Initialise the main dictionary which contains all the different tasks and their categories/lists
task_lists = {}

main_menu_options = ["1.Create List", "2.Delete Lists", "3.Open Lists", "4.Save & Exit"]
second_menu_options = ["1.Show Task","Create Tasks","Mark Tasks Complete","Remove Tasks","Go Back"]

print("Welcome to To-Do List Application") #welcome statement

#Main menu function for the To-Do list app - displays the options
def main():
    while True:
        print("Main Menu")
        for option in main_menu_options:
                print(option)
        user_main_menu_choice = int(input("Choose an option from (1,2,3,4):" ))
        if user_main_menu_choice == 1:
            print("Menu Option chosen: Create List/category for tasks")
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
    #converts the number to the key
    list_name = list(task_lists.keys())[list_delete_choice - 1] #creates a list of all key values and indexs it with the users choice to get the user choice values
    del task_lists[list_name] # removes the user choice value that was indexed stored by using the varaible above
    print(f'your list, is deleted')
    

def open_list(): #Displays a current list/category that already exist in the dictionary  
    print("Open a current list/category to view its tasks")
    for i, category in enumerate(task_lists.keys(), start=1):
        print(f"{i}.{category}")
    list_open_choice = int(input("Enter the number of the list you want to view: "))
    #converts the number to the key
    list_name = list(task_lists.keys())[list_open_choice - 1] #creates a list of all key values and indexs it with the users choice to get the user choice values
    print(f"You are now inside: {list_name} list!!!")
    
    #This is the second list menu where it has options to changes on that specific list like add tasks to that list
    
    while True:
        print("Task Menu")
        for option in second_menu_options:
                print(option)
        user_task_menu_choice = int(input("Choose an option from (1,2,3,4):" ))
        if user_task_menu_choice == 1:
            print("Task menu Option chosen: Create List/category for tasks")
            #display tasks if there is any
        elif user_task_menu_choice == 2:
            print("Task menu Option chosen: Create Tasks ")
            #Create new tasks in the list chosen
        elif user_task_menu_choice == 3:
            print("Task menu Option chosen: Mark tasks you've completed")
        elif user_task_menu_choice == 4:
            print("Task menu Option chosen: Show tasks")
            #Deletes lists based on user option in the list
        elif user_task_menu_choice == 5:
            print("Task menu Option chosen: Save & Exit ")
            #Exits the task menu and goes back to the Main Menu
        else:
            print("Your answer was invalid please enter a number from 1,2,3,4 correctly")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #shows tasks inside the lists
    if len(task_lists[list_name]) == 0:
        print("You have not tasks in this list")
    else:
        for tasks in task_lists[list_name]:
            print(f'- {tasks}')
    



'''
def save_exit(): #programs closes
     
#My second menu when you choose to open a list, then for example choose to mark tasks complete
def list_menu(): #second menu
    
def add_task(): #add tasks/adds values to an individual catorgy list that was chosen
     
def mark_task_complete(): #marks the tasks complete so when viewing open lists to view tasks it show complete
     
def view_tasks():
     
def return_main_menu(): #goes to main menu '''

main()
     