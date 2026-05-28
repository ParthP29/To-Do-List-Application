'''This is my To-Do list Application which is the minimum vaible product
This program allows users to add and manage daily tasks'''
#import module to save the user data
import json
#Initialise the main dictionary which contains all the different tasks and their categories/lists
task_lists = {}

#The external file to open to write, read, and append to
FILENAME = "to_do_save_dictionary.txt"
#The menus lists with all options
main_menu_options = ["1.Create List", "2.Delete Lists", "3.Open Lists", "4.Save & Exit"]
second_menu_options = ["1.Show Task","2.Create Tasks","3.Mark Tasks Complete","4.Remove Tasks","5.Go Back"]

print("Welcome to To-Do List Application") #welcome statement


def load_previous_data(): 
    with open(FILENAME, "r") as f: #uses the json module that was imported and opens the file to read the info to use the variable in the main code.
        return json.load(f)
    
#if user wants to load previous data it saves the data as the main dictionary
load_user_choice = input("Do you want to load prevous saved data/continue your session from before")
if load_user_choice == 'yes':
    task_lists = load_previous_data() #Inialises the main dicationary as the dict that was saved in the previous program runs with the previous data/lists/tasks. 

#Main menu function for the To-Do list app - displays the options
def main():
    while True:
        print("Main Menu")
        for option in main_menu_options:  #loops through options for the main menu and displays them
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
        elif user_main_menu_choice == 4:
            print("Menu Option chosen: Save & Exit ")
            save_exit_write_file()
            break
        else:
            print("Your answer was invalid please enter a number from 1,2,3,4 correctly")

def create_list(): #adds a list that the user creates to the main dictionary of the catogries
    print("Create a category/list for your tasks to fall under") 
    name_list = input("Create a name for the list: ")
    
    #Creates  a new emtpy list inside the dictionary
    task_lists[name_list] = []
    print(task_lists)
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
    del task_lists[list_name] # removes the user choice value that was indexed and stored by using the varaible above
    print(f'your list, is deleted')
    

#Displays a current list/category that already exist in the dictionary
#Then display the second menu for task options (for eg. you can mark tasks)
def open_list():    
    print("Open a current list/category to view its opions")
    for i, category in enumerate(task_lists.keys(), start=1):
        print(f"{i}.{category}")
    list_open_choice = int(input("Enter the number of the list you want to view: "))
    #converts the number to the key
    list_name = list(task_lists.keys())[list_open_choice - 1] #creates a list of all key values and indexs it with the users choice to get the user choice values
    print(f"You are now inside: {list_name} list!!!")
    
    #This is the second list menu where it has options to changes on that specific list like add tasks to that list
    
    while True:
        print("Task Menu")
        for option in second_menu_options: #loops through options in the second task menu lists and displays them
                print(option)
        user_task_menu_choice = int(input("Choose an option from (1,2,3,4):" ))
        if user_task_menu_choice == 1:
            print("Task menu Option chosen: Shows Tasks")
            #shows tasks inside the lists
            if len(task_lists[list_name]) == 0:
                print("You have not tasks in this list")
            else:
                for tasks in task_lists[list_name]:
                    print(f'- {tasks}')
                    #display tasks if there is any

        elif user_task_menu_choice == 2:  #add tasks/adds values to an individual catorgy list that was chosen
            print("Task menu Option chosen: Create Tasks ")
            #Create new tasks in the list chosen
            task = input("enter the task you want to add")
            task_lists[list_name].append(task)
            print(f"{task} task is added to {list_name}")

        elif user_task_menu_choice == 3: #marks the tasks complete so when viewing open lists to view tasks it shows complete
            print("Task menu Option chosen: Mark tasks you've completed")
            if len(task_lists[list_name]) == 0:
                print("You have not tasks in this list")
            #mark item complete
            else:
                print("Tasks:")
                for i, task in enumerate(task_lists[list_name], start=1):
                    print(f'{i}.{task}')

                complete_task_choice = int(input("Enter the number of which task you have completed and wanna mark of: "))
                tasks_text_info = task_lists[list_name][complete_task_choice - 1] #stores the tasks text info by indexing the list name in the main dict and then indexing values as a list by using the complete choice
                task_lists[list_name][complete_task_choice - 1] = tasks_text_info + " --> completed" #then adds a tick to that task
                print(f"{tasks_text_info} is marked complete") 

        elif user_task_menu_choice == 4:
            print("Task menu Option chosen: Delete Tasks")
            #Deletes lists based on user option in the list
            print("Tasks:")
            for i, task in enumerate(task_lists[list_name], start=1):
                print(f'{i}.{task}')
            
            task_delete_choice = int(input("Enter the number of the task you want to delete: "))
            task_deleted = task_lists[list_name].pop(task_delete_choice - 1)

        elif user_task_menu_choice == 5:
            print("Task menu Option chosen: Go Back To Main Menu ")
            #Exits the task menu and goes back to the Main Menu
            break
        else:
            print("Your answer was invalid please enter a number from 1,2,3,4 correctly")

def save_exit_write_file(): #programs closes and saves by writing contents to file
  #saves dictionary and lists data to save all the previous tasks and categories for the lists
  save_data = input("Do you want to save your data")
  if save_data == "yes":
      print('HI')
      with open(FILENAME, "w") as f:  #opens the save dictioanry file and overwrites the main variable dictionary 'task_lists' into the file.
          json.dump(task_lists, f)
  else:
        print("Goodbye")  

main()
     