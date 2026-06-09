''' This is my version 3 of my To-Do list Application which is very visually appealling
as im going to use Pillow library to boost the attraction of the layout and app by integrating very appealing 
images/visual plus a nice colour scheme to make the user more engaged.'''
#Import modules and import module to save the files main dictionary 
import tkinter as tk
from tkinter import messagebox
import json
from PIL import Image, ImageTk
#creating & naming the main window for the application
window = tk.Tk()
window.geometry("440x500")
window.title("To-Do List Application")
#Allow resizing
window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)

#Initialise the main dictionary which contains all the different tasks and their categories/lists
task_lists = {
    }

#The external file to open to write, read, and append to
FILENAME = "to_do_save_dictionary.txt"
#Constant fonts
FONT = font=("Calibri", 12) #Font for Headings
FONT_SMALLER = font=("Calibri", 11) #Font for subheadings and text beneath

#Creating the frames
#login page 1
login_frame = tk.Frame(window,background="lightblue")
login_frame.grid(row=0, column=0, sticky="nsew")
login_frame.grid_columnconfigure(0, weight=1)
#load previous Page 2 
start_load_frame = tk.Frame(window, background='lightblue')
start_load_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")
#two frame in same window both showing with top frame and middle frame
#Main Menu Page 3
#nav bar
top_main_menu_frame = tk.Frame(window, bg="navyblue") 
top_main_menu_frame.grid(row=0, column=0, sticky="nsew")
top_main_menu_frame.grid_columnconfigure(0, weight=1) 
for i in range(4): #makes each button in the nav expand eqaully
    top_main_menu_frame.grid_columnconfigure(i, weight=1)
#middle content main component 1
middle_main_menu_frame = tk.Frame(window, bg="lightblue", height=100) 
middle_main_menu_frame.grid(row=1, column=0, sticky="nsew")
middle_main_menu_frame.grid_columnconfigure(0, weight=1)
middle_main_menu_frame.grid_columnconfigure(1, weight=1)
#Task Menu Page 4
#task 2nd menu nav bar
top_task_menu_frame = tk.Frame(window, background="navyblue")
top_task_menu_frame.grid(row=0, column=0, sticky="nsew")
top_task_menu_frame.grid_columnconfigure(0, weight=1)
top_task_menu_frame.grid_columnconfigure(1, weight=1)
for i in range(5): #makes each button in the task option nav expand eqaully as they each have eqaul weight/size in the column
   top_task_menu_frame.grid_columnconfigure(i, weight=1)
#middle content main component 2
middle_task_menu_frame = tk.Frame(window, background="lightblue")
middle_task_menu_frame.grid(row=1, column=0, sticky="nsew")
middle_task_menu_frame.grid_columnconfigure(0, weight=1)
middle_task_menu_frame.grid_columnconfigure(1, weight=1)

#welcome statement
start_load_frame.tkraise()
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
load_previous_label = tk.Label(start_load_frame, text="Do you want to load prevous saved data/continue your session from before", background='lightblue',  font=FONT)
load_previous_label.grid(row=0, column=0, columnspan=2, pady=20)
#Yes or No button for the user choice
load_saved_data_button = tk.Button(start_load_frame, text="Yes, Load", command=lambda:load_previous_data("yes"), background="lightgrey")
load_saved_data_button.grid(row=1, column=0, padx=10, sticky='ew')

no_saved_data_button = tk.Button(start_load_frame, text="No, New session", command=lambda:load_previous_data("no"), background="lightgrey")
no_saved_data_button.grid(row=1, column=1, padx=10, sticky='ew')

#loading the logo
def images_app_main():
    global logo_img, create_list_img, mark_task_img, create_task_img, delete_task_img, save_exit_img
    logo = Image.open("logo.png")
    logo = logo.resize((100, 35))
    logo_img = ImageTk.PhotoImage(logo) #convert the image to tkinter form
    #placing in top frame with Main Menu label and Task Menu label
    logo_label = tk.Label(top_main_menu_frame, image=logo_img, background="navyblue")
    logo_label.image = logo_img
    logo_label.grid(row=0, column=0,columnspan=2, sticky="e")

    logo_label2 = tk.Label(top_task_menu_frame, image=logo_img, background="navyblue")
    logo_label2.image = logo_img
    logo_label2.grid(row=0, column=1,sticky="e")
    
    #Image under create lists create an image for attraction
    create_list_phto = Image.open("createlist.png")
    create_list_phto = create_list_phto.resize((250, 250)) 
    create_list_img = ImageTk.PhotoImage(create_list_phto)#convert the image to tkinter form

    #Image under create tasks create an image for attraction
    create_task_phto = Image.open("createtask.png")
    create_task_phto = create_task_phto.resize((250, 250)) 
    create_task_img = ImageTk.PhotoImage(create_task_phto)#convert the image to tkinter form

    #Image under mark tasks complete create an image for attraction
    mark_task_phto = Image.open("marktask.png")
    mark_task_phto = mark_task_phto.resize((25, 25)) 
    mark_task_img = ImageTk.PhotoImage(mark_task_phto)#convert the image to tkinter form

    #Image for the delete Tasks and lists
    delete_task_photo = Image.open("delete.png")
    delete_task_photo = delete_task_photo.resize((60,67))
    delete_task_img = ImageTk.PhotoImage(delete_task_photo)#convert the image to tkinter form

    #Images icon for the save and exit option
    save_exit_photo = Image.open("save_exit.png")
    save_exit_photo = save_exit_photo.resize((60, 60))
    save_exit_img = ImageTk.PhotoImage(save_exit_photo) #convert the image to tkinter form

#Clear all 
def clear_middle_frames():
    for widget in middle_main_menu_frame.winfo_children():
        widget.destroy()
    for widget in middle_task_menu_frame.winfo_children():
        widget.destroy()

#Main menu function for the To-Do list app - displays the options
def main_menu():
    menu_label = tk.Label(top_main_menu_frame, text="MAIN MENU", font=35,background="navyblue",fg="white", anchor="w", padx=5) #Titles the main MENU
    menu_label.grid(row=0,column=2, columnspan=2, sticky="nsew")

    #buttons for each options
    #Create Lists button
    create_list_button = tk.Button(top_main_menu_frame, text="Create List", command=create_list, background="lightgrey")
    create_list_button.grid(row=1,column=0,padx=5,pady=10, sticky="ew")
    #Delete Lists button
    delete_lists_button = tk.Button(top_main_menu_frame, text="Delete List", command=delete_lists, background="lightgrey")
    delete_lists_button.grid(row=1,column=1,padx=5, pady=10, sticky="ew")
    #Open List button
    open_list_button = tk.Button(top_main_menu_frame, text="Open List", command=open_list, background="lightgrey")
    open_list_button.grid(row=1,column=2,padx=5,pady=10, sticky="ew")
    #Save & Exit
    save_exit_button = tk.Button(top_main_menu_frame, text="Save & Exit", command=save_exit_write_file, background="lightgrey") 
    save_exit_button.grid(row=1,column=3,padx=5,pady=10, sticky="ew")

def save_list(name_list_entry): #gets the entry of the create list name and stores it in the dictionary then clear the text box 
    save_list_name = name_list_entry.get()
    #Creates  a new emtpy list inside the dictionary
    if save_list_name.strip() == "": #takes away all empty spaces and check if there is still any input
        messagebox.showerror("Invalid Task", "Please enter a valid task name") #print error message if no input
        name_list_entry.delete(0, tk.END) #removes the input in the entry box of empty spaces
        return
    elif save_list_name:
        task_lists[save_list_name] = [] 
        name_list_entry.delete(0, tk.END) #removes the input in the entry box
        #tells user that list is acutally created
        messagebox.showinfo("List Created", f"Your list {name_list_entry} has been created") #notfiies the user the list has been created
    else:
        messagebox.showerror("error","Please Enter A Valid Input") #title of window, then error message if nothing is entered

def create_list(): #adds a list that the user creates to the main dictionary of the catogries
    clear_middle_frames()
    create_list_label = tk.Label(middle_main_menu_frame, text="Create a category/list for your tasks to fall under", padx=10, font=FONT) 
    create_list_label.grid(row=0, column=0, columnspan=3, pady=17)
    name_list_label = tk.Label(middle_main_menu_frame, text="Create Name: ", font=FONT_SMALLER)
    name_list_label.grid(row=1, column=0, sticky="nsew", pady=4)
    name_list_entry = tk.Entry(middle_main_menu_frame)
    name_list_entry.grid(row=1, column=1, sticky="nsew", pady=4)
    sumbit_button = tk.Button(middle_main_menu_frame, text="Create List", command=lambda: save_list(name_list_entry), font=FONT_SMALLER)
    sumbit_button.grid(row=1,column=2, padx=1, pady=4)
    #placing image in create lists area
    create_img_label = tk.Label(middle_main_menu_frame, image=create_list_img)
    create_img_label.image = create_list_img
    create_img_label.grid(row=3, column=0, columnspan=3, pady=15)

#takes the list button clicked and removes it from the main dictionary
def confirm_delete_list(category):
    del task_lists[category] # removes the user choice value that was indexed and stored by using the varaible above
    delete_lists()
    confirmation_del = tk.Label(middle_main_menu_frame, text=f"{category} was deleted from the data!!!")
    confirmation_del.grid(row=2, column=0, columnspan=2, pady=10)
#Deletes a list
def delete_lists(): 
    clear_middle_frames() #clears all the labels,buttons, and entry boxes in the middle frame
    global task_lists
    delete_list_label = tk.Label(middle_main_menu_frame, text="Delete any lists you wouldn't like!!!", font=FONT)
    delete_list_label.grid(row=0,column=0, columnspan=2, pady=17)
    delete_task_imglabel = tk.Label(middle_main_menu_frame, image=delete_task_img, anchor="e")
    delete_task_imglabel.image = delete_task_img
    delete_task_imglabel.grid(row=1, column=1, sticky="w", pady=5)
    Av_list_label = tk.Label(middle_main_menu_frame, text="Available Lists:", font=FONT)
    Av_list_label.grid(row=2, column=0, columnspan=2, pady=8)
    if len(task_lists) == 0: #if no lists are already in the task lists dictionary.
        messagebox.showinfo("Delete Lists","There no current lists to delete go to menu and create one")
    else:
        for i, category in enumerate(task_lists.keys(), start=1):
            list_delete_button = tk.Button(middle_main_menu_frame, text=f"{category}", command=lambda category=category:confirm_delete_list(category), font=FONT, width=75)
            list_delete_button.grid(row=3+i,column=0, columnspan=2, pady=5,padx=40)

#Displays a current list/category that already exist in the dictionary
def switch_pages():
    top_task_menu_frame.tkraise()
    middle_task_menu_frame.tkraise()

#This is the second task menu page where it has options to changes on that specific list like add tasks to that list
#before open lists so i can call it in open_lists
def task_menu():   
    task_menu_label = tk.Label(top_task_menu_frame, text="TASK MENU", font=25,  background="navyblue", fg="white", anchor="w") #Titles the TASK 2nd MENU
    task_menu_label.grid(row=0, column=2, sticky='w')

    #buttons for each options
    #Displays the Tasks in that list button
    create_list_button = tk.Button(top_task_menu_frame, text="Show Tasks", command=show_tasks, background="lightgrey")
    create_list_button.grid(row=1,column=0,padx=2,pady=10, sticky="ew")
    #Creating Tasks button
    delete_lists_button = tk.Button(top_task_menu_frame, text="Create Tasks", command=create_tasks, background="lightgrey")
    delete_lists_button.grid(row=1,column=1,padx=2,pady=10, sticky='ew')
    #Marking the task user finished complete button
    open_list_button = tk.Button(top_task_menu_frame, text="Mark Tasks Complete", command=mark_tasks, background="lightgrey")
    open_list_button.grid(row=1,column=2,padx=2,pady=10, sticky='ew')
    #Remove Tasks button
    save_exit_button = tk.Button(top_task_menu_frame, text="Remove Tasks", command=delete_task, background="lightgrey") 
    save_exit_button.grid(row=1,column=3,padx=2, pady=10, sticky='ew')
    #Go back to main menu page button
    save_exit_button = tk.Button(top_task_menu_frame, text="Go back", command=go_back, background="lightgrey") 
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
    open_list_label = tk.Label(middle_main_menu_frame, text="Open a current list/category to view its opions!!!", font=FONT)
    open_list_label.grid(row=0,column=0,columnspan=2, pady=17)
    Av_list_label = tk.Label(middle_main_menu_frame, text="Available Lists:", font=FONT)
    Av_list_label.grid(row=1, column=0, columnspan=2)
    if len(task_lists) == 0: #if no lists are already in the task lists dictionary.
        messagebox.showinfo("Open Lists","There no current lists to open go to menu and create one")
    else:
        for i, category in enumerate(task_lists.keys(), start=1):
            #when list chosen to open it leads to this the options task menu 2nd page 
            list_open_button = tk.Button(middle_main_menu_frame, text=f"{category}", command=lambda category=category:open_select_confirm(category), font=FONT_SMALLER, width=50)
            list_open_button.grid(row=2+i,column=0,columnspan=2, pady=10)
    task_menu()

#Then display the second menu for task options (for eg. you can mark tasks)
#functions for each option from the task menu
def show_tasks():
    clear_middle_frames()
    global current_category
    show_task_label = tk.Label(middle_task_menu_frame, text="Tasks Display", font=FONT)
    show_task_label.grid(row=1, column=0,columnspan=2, pady=17)
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
        tk.Label(middle_task_menu_frame, text="TO DO", background="darkgrey", font=FONT).grid(row=2, column=0, pady=10,padx=10, sticky='ew')

        for i, task in enumerate(todo):
            to_do_tasks = tk.Label(middle_task_menu_frame, text=task, font=FONT_SMALLER)
            to_do_tasks.grid(row=3+i, column=0, pady=10, padx=20, sticky='ew')

        #completed tasks 
        tk.Label(middle_task_menu_frame, text="COMPLETED", background="darkgrey", font=FONT).grid(row=2, column=1, pady=10, padx=10, sticky='ew')

        for i, task in enumerate(completed):
            completed_tasks = tk.Label(middle_task_menu_frame, text=task, font=FONT_SMALLER)
            completed_tasks.grid(row=3+i, column=1, pady=10, padx=20, sticky='ew') 
            

def save_task(task_entry):
    save_task_name = task_entry.get()
    if save_task_name.strip() == "":
        messagebox.showerror("Invalid Task", "Please enter a valid task name")
        return
    #Creates  a new emtpy list inside the dictionary
    else:
        task_lists[current_category].append(save_task_name)
        #tells user that list is acutally created
        messagebox.showinfo("Task Created", f"Your list {save_task_name} has been created and added to {current_category}")
        task_entry.delete(0, tk.END) #removes the input in the entry box

def create_tasks():
    clear_middle_frames()
#add tasks/adds values to an individual catorgy list that was chosen
    create_tasks_label = tk.Label(middle_task_menu_frame, text="Create Tasks ", font=FONT)
    create_tasks_label.grid(row=0,column=0, columnspan=2, pady=17)
    #Create new tasks in the list chosen
    task_entry = tk.Entry(middle_task_menu_frame)
    task_entry.grid(row=1, column=0, sticky="nesw")
    task_submit_button = tk.Button(middle_task_menu_frame, text="Sumbit Task", command=lambda:save_task(task_entry), font=FONT_SMALLER)
    task_submit_button.grid(row=1, column=1, sticky="ew")
    #This is the image in the create tasks section
    create_task_imglabel = tk.Label(middle_task_menu_frame, image=create_task_img, anchor="w")
    create_task_imglabel.image = create_task_img
    create_task_imglabel.grid(row=2, column=0, columnspan=2, pady=15)

def mark_task_complete(i):
    if "✔" in task_lists[current_category][i]:
        messagebox.showinfo("Marked Task","Task Already Marked Complete")
        return
    task_lists[current_category][i] += " ✔"
    mark_tasks()    
    confirmation_mark = tk.Label(middle_task_menu_frame, text=f"Marked Complete: {task_lists[current_category][i]}",  font=FONT_SMALLER)
    confirmation_mark.grid(row=3, column=0, columnspan=2)

def mark_tasks():
    clear_middle_frames()
    #user_task_menu_choice == 3: #marks the tasks complete so when viewing open lists to view tasks it shows complete
    mark_task_label = tk.Label(middle_task_menu_frame, text="            Mark tasks you've completed", width=80, font=FONT)
    mark_task_label.grid(row=0,column=1, columnspan=3, sticky='w', pady=17)
    #This is the image in the mark tasks complete section
    mark_task_imglabel = tk.Label(middle_task_menu_frame, image=mark_task_img)
    mark_task_imglabel.image = mark_task_img
    mark_task_imglabel.grid(row=0, column=1, sticky="w", pady=15)
    task_label = tk.Label(middle_task_menu_frame, text="Tasks:", font=FONT, width=50).grid(row=1, column=0, columnspan=2,pady=10)
    if len(task_lists[current_category]) == 0:
        messagebox.showinfo("Mark Tasks", "You have not tasks in this list")
        #mark item complete
    else:
        for i, task in enumerate(task_lists[current_category]):
            if "✔" not in task:
                mark_task_button = tk.Button(middle_task_menu_frame, text=f'{task}',font=FONT_SMALLER, command=lambda i=i:mark_task_complete(i), width=50)
                mark_task_button.grid(row=4+i, column=0,columnspan=5, padx=30,pady=10)

#takes the specific task button clicked and removes it from the main dictionary
def confirm_delete_task(task):
    task_lists[current_category].remove(task)
    delete_task()
    confirmation_del = tk.Label(middle_task_menu_frame, text=f"{task} was deleted from the data!!!", font=FONT_SMALLER)
    confirmation_del.grid(row=2, column=0, columnspan=2)

#Deletes a task
def delete_task(): 
    clear_middle_frames()
    global task_lists
    delete_task_label = tk.Label(middle_task_menu_frame, text="Delete any Tasks you wouldn't like!!!",  font=FONT)
    delete_task_label.grid(row=0, column=0,columnspan=2, pady=17)
    delete_task_imglabel = tk.Label(middle_task_menu_frame, image=delete_task_img, anchor="e")
    delete_task_imglabel.image = delete_task_img
    delete_task_imglabel.grid(row=2, column=1,pady=7, sticky="w")
    Av_list_label = tk.Label(middle_task_menu_frame, text="Available Tasks:",font=FONT_SMALLER )
    Av_list_label.grid(row=3, column=0, columnspan=2)
    if len(task_lists[current_category]) == 0: #if no tasks are already in the task lists dictionary.
        messagebox.showinfo("Delete Tasks","There no current Tasks to delete go to task menu and create one")
    else:
        for i, task in enumerate(task_lists[current_category], start=1):
            task_delete_button = tk.Button(middle_task_menu_frame, text=f'{task}', command=lambda task=task: confirm_delete_task(task), font=FONT_SMALLER, width=50)
            task_delete_button.grid(row=4+i,column=0,columnspan=2, pady=10)
#Exits the task menu and goes back to the Main Menu
def go_back():
    top_main_menu_frame.tkraise() #raise/brings forward the top frame from the main menu page
    middle_main_menu_frame.tkraise() #raise/brings forward the middle frame from the main menu page


def save_exit_button():
    clear_middle_frames()
    with open(FILENAME, "w") as f:  #opens the save dictioanry file and overwrites the main variable dictionary 'task_lists' into the file.
        json.dump(task_lists, f)
    tk.Label(middle_main_menu_frame, text="Goodbye").grid(row=0, column=0, columnspan=2, sticky='ew')
    window.destroy()

#programs closes and saves by writing contents to file
def save_exit_write_file(): 
  clear_middle_frames() #clear all the labels,buttons, and entry boxes in the middle frame for the next new option clicked function to show up
  #saves dictionary and lists data to save all the previous tasks and categories for the lists
  save_data_label = tk.Label(middle_main_menu_frame, text="Exit - Do you want to save your session before exiting?", font=FONT)
  save_data_label.grid(row=0, column=0,columnspan=2, padx=10, pady=20)
  #image icon for save and exit
  save_exit_imglabel = tk.Label(middle_main_menu_frame, image=save_exit_img, anchor="e")
  save_exit_imglabel.image = save_exit_img
  save_exit_imglabel.grid(row=1, column=0,columnspan=2)
  #Yes button to save the data
  save_yes_btn = tk.Button(middle_main_menu_frame, text="YES", font=FONT_SMALLER, command=save_exit_button)
  save_yes_btn.grid(row=2, column=0, sticky='nsew', padx=10, pady=20)
  #no button to not save the data
  save_no_btn = tk.Button(middle_main_menu_frame, text="NO", font=FONT_SMALLER, command=lambda:window.destroy(), height=2)
  save_no_btn.grid(row=2, column=1, sticky='nsew', padx=10, pady=20)  

def main(): #runs all function in the program
    images_app_main() #first page - login page #############################################################################################################################
    main_menu() #Runs the main function of the program which call all other function in the program 

main()
window.mainloop() #Continue the flow of the program and continues when something is clicked or entered