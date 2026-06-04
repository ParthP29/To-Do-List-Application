''' This is my version 2 of my To-Do list Application which is very visually appealling
as im going to use Tkinter to boost the attraction the most, while fixing invalid type input
errors to stop crashes and improve reliabilty for the user'''
#Import modules and import module to save the files main dictionary 
import tkinter as tk
from tkinter import messagebox
import json
#creating & naming the main window for the application
window = tk.Tk()
window.geometry("440x500")
window.title("To-Do List Application")
#Allow resizing
window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)
#Creating the frames
start_load_frame = tk.Frame(window)
start_load_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")
#two frame in same window both showing
#Main Menu Page 1
#nav bar
top_main_menu_frame = tk.Frame(window, bg="blue") 
top_main_menu_frame.grid(row=0, column=0,columnspan=5, sticky="nsew")
top_main_menu_frame.grid_columnconfigure(0, weight=1) 
for i in range(4): #makes each button in the nav expand eqaully
    top_main_menu_frame.grid_columnconfigure(i, weight=1)
    
#main component
middle_main_menu_frame = tk.Frame(window, bg="red", height=100) 
middle_main_menu_frame.grid(row=1, column=0, sticky="nsew")
middle_main_menu_frame.grid_columnconfigure(0, weight=1)
#Task Menu Page 2
top_task_menu_frame = tk.Frame(window, bg="lightgray")
top_task_menu_frame.grid(row=0, column=0, sticky="nsew")
top_task_menu_frame.grid_columnconfigure(0, weight=1)
for i in range(5): #makes each button in the task option nav expand eqaully
    top_task_menu_frame.grid_columnconfigure(i, weight=1)

middle_task_menu_frame = tk.Frame(window, bg="darkgray")
middle_task_menu_frame.grid(row=1, column=0, sticky="nsew")
middle_task_menu_frame.grid_columnconfigure(0, weight=1)
middle_task_menu_frame.grid_columnconfigure(1, weight=1)

#Initialise the main dictionary which contains all the different tasks and their categories/lists
task_lists = {
    "Shopping":["apples","bananas","pear"],
    "Homework":["Maths"],
    "Other":[]
    }

#The external file to open to write, read, and append to
FILENAME = "to_do_save_dictionary.txt"

print("Welcome to To-Do List Application") #welcome statement

start_load_frame.tkraise() #raises the starting frame for the first page

#if user wants to load previous data it saves the data as the main dictionary
def load_previous_data(choice):
    global task_lists 
    if choice == "yes":
        try:
            with open(FILENAME, "r") as f: #uses the json module that was imported and opens the file to read the info to use the variable in the main code.
                task_lists = json.load(f) #Inialises the main dicationary as the dict that was saved in the previous program runs with the previous data/lists/tasks. 
        except FileNotFoundError:
            no_file_label = tk.Label(window, text="No file found new session starting...")
            task_lists = {} #if no file exists start empty one
    elif choice == "no":
        task_lists = {}
    top_main_menu_frame.tkraise()
    middle_main_menu_frame.tkraise() #bring the main frame to the front

#labels of asking user if they want to load the previously saved sessions  
load_previous_label = tk.Label(start_load_frame, text="Do you want to load prevous saved data/continue your session from before")
load_previous_label.grid(row=0, column=0, columnspan=2, pady=20)
#Yes or No button for the user choice
load_saved_data_button = tk.Button(start_load_frame, text="Yes, Load", command=lambda:load_previous_data("yes"))
load_saved_data_button.grid(row=1, column=0, padx=10)

no_saved_data_button = tk.Button(start_load_frame, text="No, New session", command=lambda:load_previous_data("no"))
no_saved_data_button.grid(row=1, column=1, padx=10)
#Clear all 
def clear_middle_frames():
    for widget in middle_main_menu_frame.winfo_children():
        widget.destroy()
    for widget in middle_task_menu_frame.winfo_children():
        widget.destroy()

#Main menu function for the To-Do list app - displays the options
def main():
    
    menu_label = tk.Label(top_main_menu_frame, text="MAIN MENU", font=25,) #Titles the main MENU
    menu_label.grid(row=0,column=0, columnspan=5, sticky="nsew")

    #buttons for each options
    #Create Lists button
    create_list_button = tk.Button(top_main_menu_frame, text="Create List", command=create_list)
    create_list_button.grid(row=1,column=0,padx=5,pady=10, sticky="ew")
    #Delete Lists button
    delete_lists_button = tk.Button(top_main_menu_frame, text="Delete List", command=delete_lists)
    delete_lists_button.grid(row=1,column=1, padx=5,pady=10, sticky="ew")
    #Open List button
    open_list_button = tk.Button(top_main_menu_frame, text="Open List", command=open_list)
    open_list_button.grid(row=1,column=2,padx=5,pady=10, sticky="ew")
    #Save & Exit
    save_exit_button = tk.Button(top_main_menu_frame, text="Save & Exit", command=save_exit_write_file) 
    save_exit_button.grid(row=1,column=3,padx=5,pady=10, sticky="ew")

def save_list(name_list_entry): #gets the entry of the create list name and stores it in the dictionary then clear the text box 
    save_list_name = name_list_entry.get()
    #Creates  a new emtpy list inside the dictionary
    if save_list_name:
        task_lists[save_list_name] = [] 
    #tells user that list is acutally created
        messagebox.showinfo("List Created", f"Your list {name_list_entry} has been created")
        name_list_entry.delete(0, tk.END) #removes the input in the entry box
    else:
        messagebox.showerror("error","Please Enter A Valid Input") #title of window, then error message if nothing is entered

def create_list(): #adds a list that the user creates to the main dictionary of the catogries
    clear_middle_frames()
    create_list_label = tk.Label(middle_main_menu_frame, text="Create a category/list for your tasks to fall under", padx=10) 
    create_list_label.grid(row=0, column=0, columnspan=3, pady=20)
    name_list_label = tk.Label(middle_main_menu_frame, text="Create Name: ")
    name_list_label.grid(row=1, column=0, sticky="nsew", pady=4)
    name_list_entry = tk.Entry(middle_main_menu_frame)
    name_list_entry.grid(row=1, column=1, sticky="nsew", pady=4)
    sumbit_button = tk.Button(middle_main_menu_frame, text="Create List", command=lambda: save_list(name_list_entry))
    sumbit_button.grid(row=1,column=2, padx=1, pady=4)

#takes the list button clicked and removes it from the main dictionary
def confirm_delete_list(category):
    del task_lists[category] # removes the user choice value that was indexed and stored by using the varaible above
    confirmation_del = tk.Label(middle_main_menu_frame, text=f"{category} was deleted from the data!!!")
    confirmation_del.grid(row=2, column=0, pady=10)

#Deletes a list
def delete_lists(): 
    clear_middle_frames() #clears all the labels,buttons, and entry boxes in the middle frame
    global task_lists
    delete_list_label = tk.Label(middle_main_menu_frame, text="Delete any lists you wouldn't like!!!")
    delete_list_label.grid(row=0,column=0, columnspan=2, pady=20)
    if len(task_lists) == 0: #if no lists are already in the task lists dictionary.
        messagebox.showinfo("Delete Lists","There no current lists to delete go to menu and create one")
    else:
        Av_list_label = tk.Label(middle_main_menu_frame, text="Available Lists:")
        Av_list_label.grid(row=1, column=0, columnspan=len(task_lists.keys()), pady=8)
        for i, category in enumerate(task_lists.keys(), start=1):
            list_delete_button = tk.Button(middle_main_menu_frame, text=f"{category}", command=lambda category=category:confirm_delete_list(category))
            list_delete_button.grid(row=3+i,column=0, columnspan=2, pady=5,padx=10, sticky="ew")

#Displays a current list/category that already exist in the dictionary
def switch_pages():
    top_task_menu_frame.tkraise()
    middle_task_menu_frame.tkraise()

#This is the second task menu page where it has options to changes on that specific list like add tasks to that list
#before open lists so i can call it in open_lists
def task_menu():   
    task_menu_label = tk.Label(top_task_menu_frame, text="TASK MENU", font=25,) #Titles the TASK 2nd MENU
    task_menu_label.grid(row=0, column=0, columnspan=5, sticky='ew')

    #buttons for each options
    #Displays the Tasks in that list button
    create_list_button = tk.Button(top_task_menu_frame, text="Show Tasks", command=show_tasks)
    create_list_button.grid(row=1,column=0,padx=2,pady=10, sticky="ew")
    #Creating Tasks button
    delete_lists_button = tk.Button(top_task_menu_frame, text="Create Tasks", command=create_tasks)
    delete_lists_button.grid(row=1,column=1,padx=2,pady=10, sticky='ew')
    #Marking the task user finished complete button
    open_list_button = tk.Button(top_task_menu_frame, text="Mark Tasks Complete", command=mark_tasks)
    open_list_button.grid(row=1,column=2,padx=2,pady=10, sticky='ew')
    #Remove Tasks button
    save_exit_button = tk.Button(top_task_menu_frame, text="Remove Tasks", command=delete_task) 
    save_exit_button.grid(row=1,column=3,padx=2, pady=10, sticky='ew')
    #Go back to main menu page button
    save_exit_button = tk.Button(top_task_menu_frame, text="Go back", command=go_back) 
    save_exit_button.grid(row=1,column=4,padx=2,pady=10, sticky='ew')
    
#confirmation of what task is opened and switches page
def open_select_confirm(category):
    global current_category
    current_category = category #the category (eg shopping) that the user clicked
    switch_pages()
    confirmation_open = tk.Label(middle_task_menu_frame, text = f"You are now inside: {current_category} list!!!")
    confirmation_open.grid(row=0, column=0, columnspan=2)

def open_list():
    clear_middle_frames() #clear all the labels,buttons, and entry boxes in the middle frame
    open_list_label = tk.Label(middle_main_menu_frame, text="Open a current list/category to view its opions!!!")
    open_list_label.grid(row=0,column=0, pady=20)
    if len(task_lists) == 0: #if no lists are already in the task lists dictionary.
        messagebox.showinfo("Open Lists","There no current lists to open go to menu and create one")
    else:
        Av_list_label = tk.Label(middle_main_menu_frame, text="Available Lists:")
        Av_list_label.grid(row=1, column=0)
        for i, category in enumerate(task_lists.keys(), start=1):
            #when list chosen to open it leads to this the options task menu 2nd page 
            list_open_button = tk.Button(middle_main_menu_frame, text=f"{category}", command=lambda category=category:open_select_confirm(category))
            list_open_button.grid(row=2+i,column=0, sticky="nsew", pady=10)
    task_menu()

#Then display the second menu for task options (for eg. you can mark tasks)
#functions for each option from the task menu
def show_tasks():
    clear_middle_frames()
    global current_category
    show_task_label = tk.Label(middle_task_menu_frame, text="Task menu Option chosen: Show Tasks")
    show_task_label.grid(row=1, column=0,columnspan=2, pady=20)
    #shows tasks inside the lists
    if len(task_lists[current_category])  == 0: 
        messagebox.showinfo("show tasks", "You have not tasks in this list")
    else:
        todo = []
        completed= []

        #Split task into completed and not to do
        for task in task_lists[current_category]:
            if "✔" in task:
                completed.append(task)
            else:
                todo.append(task)
        #to do tasks
        tk.Label(middle_task_menu_frame, text="TO DO", background="lightgreen").grid(row=2, column=0, pady=10,padx=10, sticky='ew')

        for i, task in enumerate(todo):
            to_do_tasks = tk.Label(middle_task_menu_frame, text=task)
            to_do_tasks.grid(row=3+i, column=0, pady=10, padx=10, sticky='ew')

        #completed tasks 
        tk.Label(middle_task_menu_frame, text="COMPLETED", background="lightblue").grid(row=2, column=1, pady=10, padx=10, sticky='ew')

        for i, task in enumerate(completed):
            completed_tasks = tk.Label(middle_task_menu_frame, text=task)
            completed_tasks.grid(row=3+i, column=1, pady=10, padx=8, sticky='ew') 
            

def save_task(task_entry):
    save_task_name = task_entry.get()
    #Creates  a new emtpy list inside the dictionary
    if save_task_name:
        task_lists[current_category].append(save_task_name)
        #tells user that list is acutally created
        messagebox.showinfo("Task Created", f"Your list {save_task_name} has been created and added to {current_category}")
        task_entry.delete(0, tk.END) #removes the input in the entry box
    else:
        messagebox.showerror("error","Please Enter A Valid Input") #title of window, then error message if nothing is entered

def create_tasks():
    clear_middle_frames()
#add tasks/adds values to an individual catorgy list that was chosen
    create_tasks_label = tk.Label(middle_task_menu_frame, text="Task menu Option chosen: Create Tasks ")
    create_tasks_label.grid(row=0,column=0, columnspan=2, pady=20)
    #Create new tasks in the list chosen
    task_entry = tk.Entry(middle_task_menu_frame)
    task_entry.grid(row=1, column=0, sticky="nesw")
    task_submit_button = tk.Button(middle_task_menu_frame, text="Sumbit Task", command=lambda:save_task(task_entry))
    task_submit_button.grid(row=1, column=1, sticky="ew")

def mark_task_complete(i):
    if "✔" in task_lists[current_category][i]:
        messagebox.showinfo("Marked Task","Task Already Marked Complete")
        return

    task_lists[current_category][i] += "✔"
    confirmation_mark = tk.Label(middle_task_menu_frame, text=f"{task_lists[current_category][i]} is Marked Complete!!!")
    confirmation_mark.grid(row=5, column=0)
    mark_tasks()

def mark_tasks():
    clear_middle_frames()
    #user_task_menu_choice == 3: #marks the tasks complete so when viewing open lists to view tasks it shows complete
    print("Task menu Option chosen: Mark tasks you've completed")
    if len(task_lists[current_category]) == 0:
        messagebox.showinfo("Mark Tasks", "You have not tasks in this list")
        #mark item complete
    else:
        print("Tasks:")
        for i, task in enumerate(task_lists[current_category]):
            if "✔" not in task:
                mark_task_button = tk.Button(middle_task_menu_frame, text=f'{task}', command=lambda i=i:mark_task_complete(i))
                mark_task_button.grid(row=5, column=3)

#takes the specific task button clicked and removes it from the main dictionary
def confirm_delete_task(task):
    task_lists[current_category].remove(task)
    confirmation_del = tk.Label(middle_task_menu_frame, text=f"{task} was deleted from the data!!!")
    confirmation_del.grid(row=2, column=0, columnspan=len(task_lists.keys()))

#Deletes a task
def delete_task(): 
    clear_middle_frames()
    global task_lists
    delete_task_label = tk.Label(middle_task_menu_frame, text="Delete any Tasks you wouldn't like!!!")
    delete_task_label.grid(row=1,column=0, sticky="ew")
    if len(task_lists) == 0: #if no tasks are already in the task lists dictionary.
        messagebox.showinfo("Delete Tasks","There no current Tasks to delete go to task menu and create one")
    else:
        Av_list_label = tk.Label(middle_task_menu_frame, text="Available Lists:")
        Av_list_label.grid(row=3, column=0)
        for i, task in enumerate(task_lists[current_category], start=1):
            task_delete_button = tk.Button(middle_task_menu_frame, text=f'{task}', command=lambda task=task: confirm_delete_task(task))
            task_delete_button.grid(row=4+i,column=0, sticky="nsew", padx=10, pady=10)

#Exits the task menu and goes back to the Main Menu
def go_back():
    top_main_menu_frame.tkraise() #raise/brings forward the top frame from the main menu page
    middle_main_menu_frame.tkraise() #raise/brings forward the middle frame from the main menu page


def save_exit_button():
    clear_middle_frames()
    print(task_lists)
    with open(FILENAME, "w") as f:  #opens the save dictioanry file and overwrites the main variable dictionary 'task_lists' into the file.
        json.dump(task_lists, f)
    tk.Label(middle_main_menu_frame, text="Goodbye")
    window.destroy()

#programs closes and saves by writing contents to file
def save_exit_write_file(): 
  clear_middle_frames() #clear all the labels,buttons, and entry boxes in the middle frame for the next new option clicked function to show up
  #saves dictionary and lists data to save all the previous tasks and categories for the lists
  save_data_label = tk.Label(middle_task_menu_frame, text="Do you want to save your session?")
  #Yes button to save the data
  save_yes_btn = tk.Button(middle_main_menu_frame, text="YES", command=save_exit_button)
  save_yes_btn.grid(row=0, column=0)

  #no button to not save the data
  save_no_btn = tk.Button(middle_main_menu_frame, text="NO", command=lambda:window.destroy())
  save_no_btn.grid(row=0, column=1)  

main() #Runs the main function of the program which call all other function in the program 
window.mainloop() #Continue the flow of the program and continues when something is clicked or entered
     