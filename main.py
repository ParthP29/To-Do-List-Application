'''This is my version 4 of my To-Do list Application which is very visually appealling
as im going to inlcude a very attractive and appealling Tkinter Login system, allowing users to store 
their personal tasks/lists seperately and privately preventing mix ups and imporving organisation and user-experience'''
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
window.rowconfigure(0, weight=0)
window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)

#Initialise the main dictionary which contains all the different tasks and their categories/lists
task_lists = {}

#The external file to open to write, read, and append to
FILENAME = "to_do_save_dictionary.txt"
#Constant fonts
FONT = font=("Calibri", 12) #Font for Headings
FONT_SMALLER = font=("Calibri", 11) #Font for subheadings and text beneath

#Creating the frames
#login page 1
login_frame = tk.Frame(window,background="lightblue")
login_frame.grid(row=0, column=0,rowspan=2, sticky="nsew")
login_frame.grid_columnconfigure(0, weight=1)
login_frame.grid_columnconfigure(1, weight=1)
#load previous Page 2 
load_prev_frame = tk.Frame(window, background='lightblue')
load_prev_frame.grid(row=0, column=0,rowspan=2, sticky="nsew")
load_prev_frame.grid_columnconfigure(0, weight=1)
load_prev_frame.grid_columnconfigure(1, weight=1)
load_prev_frame.grid_rowconfigure(0, weight=1)
load_prev_frame.grid_rowconfigure(1, weight=1)
#two frame in same window both showing with top frame and middle frame
#Main Menu Page 3
#nav bar
top_main_menu_frame = tk.Frame(window, bg="navyblue", height=10) 
top_main_menu_frame.grid(row=0, column=0, sticky="nsew")
top_main_menu_frame.grid_columnconfigure(0, weight=1)
for i in range(4): #makes each button in the nav expand eqaully
    top_main_menu_frame.grid_columnconfigure(i, weight=1)
#middle content main component 1
middle_main_menu_frame = tk.Frame(window, bg="lightblue", height=10) 
middle_main_menu_frame.grid(row=1, column=0, sticky="nsew")
middle_main_menu_frame.grid_columnconfigure(0, weight=1)
middle_main_menu_frame.grid_columnconfigure(1, weight=1)
#Task Menu Page 4
#task 2nd menu nav bar
top_task_menu_frame = tk.Frame(window, background="navyblue", height=10)
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

#welcome statement in GUI
welcome_label = tk.Label(login_frame, text="WELCOME!!!", font=FONT)
welcome_label.grid(row=1, column=0, columnspan=2, pady = 15)
#---------------------------------The Login Page---------------------------------#
#rasie and show the first login page
login_frame.tkraise()

def load_user_logins():
    try:
        with open(FILENAME, "r") as f: #uses the json module that was imported and opens the file to read the info to use the variable in the main code.
            return json.load(f) #Inialises the main dicationary as the dict that was saved in the previous program runs with the previous data/lists/tasks. 
    except FileNotFoundError:
            no_file_label = tk.Label(window, text="No file found new session starting...")
            return {} #if no file exists start empty one
def save_users():
    with open(FILENAME, "w") as f: #uses the json module that was imported and opens the file to read the info to use the variable in the main code.
        json.dump(users, f, indent=4) #Inialises the main dicationary as the dict that was saved in the previous program runs with the previous data/lists/tasks. 

users = load_user_logins() #the users is all items in the dictionary in the saved file
current_user = None #intialising the variable with no value 

def login_system(login_name_entry, login_password_entry):
    global current_user
    
    name = login_name_entry.get().strip().lower()
    password = login_password_entry.get().strip()
    if name == "" or password == "":
        messagebox.showerror("invalid", "Please enter a valid name and password")
        return 
    
    if len(password) < 4:
        messagebox.showerror("weak Password", "Please make a stronger/longer password")
        return
    if len(name) <2:
        messagebox.showerror("Name","Name is to short, Must enter you FULL NAME (2 character min)")  

    if name.replace(" ","").isalpha(): #checks if the name is aphlabetical by firstly removing the spaces
        pass
    else: #if not then gives and error msg and lets the user try again.
        messagebox.showerror("Name","Name cannot contain a special character/number please correctly enter your full name again")    
        return
    
    #Check if its an existing users and if their password is correct
    if name in users:
        if users[name]["password"] == password:
            current_user = name
            load_previous_data() # loads the page where user is asked to load their previous data eg task and lists
            load_prev_frame.tkraise() #raises the starting frame for the next page
        else:
            messagebox.showerror("Incorrect", "Password Entered is wrong, Try Again!!!")
            return
    else: #If user does not exist then create new acocunt
        users[name] = {"password": password, #appends the new name and password log in to users 
                       "task_lists":{}} #This is where their lists will go in
        current_user = name
        save_users() #This adds the values to users which is then all writed to the saved file
        load_previous_data()
        load_prev_frame.tkraise() #raises the starting frame for the next page
    

#The login page system
def login_page():
    login_label = tk.Label(login_frame, text="LOGIN!", anchor="w", background="navyblue", font=("segoe", 12, "bold"), fg="white")
    login_label.grid(row=0, column=1, sticky='nsew')
    login_info_label = tk.Label(login_frame,pady=20, text="Enter your name and password\nNew accounts will be automatically created\nUse same login next time")
    login_info_label.grid(row=2, column=0, columnspan=2, padx=10, sticky="ew")    
    login_name_label = tk.Label(login_frame, text="Enter your Full Name:")
    login_name_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
    login_name_entry = tk.Entry(login_frame)
    login_name_entry.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
    login_password_label = tk.Label(login_frame, text="Enter your Password:")
    login_password_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
    login_password_entry = tk.Entry(login_frame)
    login_password_entry.grid(row=6, column=0,columnspan=2, padx=10, pady=10, sticky="ew")
    login_sumbit_btn = tk.Button(login_frame, text="LOG IN", command=lambda:login_system(login_name_entry,login_password_entry))
    login_sumbit_btn.grid(row=7, column=0, padx=10, pady=10, sticky="ew")
    skip_login_btn = tk.Button(login_frame, text="SKIP", command=lambda:load_previous_system("nothing")) #nothing is not an option from the if elif statment so it passes through the if statments and just raises the two frames
    skip_login_btn.grid(row=7, column=1, padx=10, pady=10, sticky="ew")


#if user wants to load previous data it saves the data as the main dictionary
def load_previous_system(choice):
    global task_lists 
    if choice == "yes": #yes is the choice value the buttons is assigned with when called in command in the load_previous_data() function
        task_lists = users[current_user]["task_lists"]
    elif choice == "no":
        task_lists = {}
    top_main_menu_frame.tkraise()
    middle_main_menu_frame.tkraise() #bring the main frame to the front

#labels of asking user if they want to load the previously saved sessions  
def load_previous_data():
    logged_in_confirm = tk.Label(load_prev_frame, text=f"{current_user} logged in!!! (if new acocunt then created)", background="lightgrey", font=("Segeo", 13), wraplength=400)
    logged_in_confirm.grid(row=1, column=0,columnspan=2, pady=1)
    load_previous_label = tk.Label(load_prev_frame, text="Do you want to load previous saved data from before", background='lightblue',  font=("Segeo", 13))
    load_previous_label.grid(row=2, column=0, columnspan=2, pady=1)
    #Yes or No button for the user choice
    load_saved_data_button = tk.Button(load_prev_frame, text="Yes, Load", command=lambda:load_previous_system("yes"), background="lightgrey", font=FONT, width=50)
    load_saved_data_button.grid(row=3, column=0, padx=10, pady=15)

    no_saved_data_button = tk.Button(load_prev_frame, text="No, New session", command=lambda:load_previous_system("no"), background="lightgrey",font=FONT, width= 50)
    no_saved_data_button.grid(row=3, column=1, padx=10, pady=40)

#------------------------------New Page Main Menu (lists) ---------------------------------------#
#loading the logo
def images_app_main():
    global logo_img, create_list_img, mark_task_img, create_task_img, delete_task_img, save_exit_img
    logo = Image.open("logo.png")
    logo = logo.resize((100, 35))
    logo_img = ImageTk.PhotoImage(logo) #convert the image to tkinter form
    #placing in top frame with Main Menu label 
    logo_label = tk.Label(top_main_menu_frame, image=logo_img, background="navyblue")
    logo_label.image = logo_img
    logo_label.grid(row=0, column=0,columnspan=2, sticky="e")

    #Placing in the top frame with task menu label
    logo_label2 = tk.Label(top_task_menu_frame, image=logo_img, background="navyblue")
    logo_label2.image = logo_img
    logo_label2.grid(row=0, column=1,sticky="e")
    
    #placing it in the login page at the top as a open app page image
    logo_label3 = tk.Label(login_frame, image=logo_img, background="navyblue", anchor='e')
    logo_label3.image = logo_img
    logo_label3.grid(row=0, column=0, sticky="nswe")
    
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
        messagebox.showerror("Invalid Task", "Please enter a valid task name") #displays error message if no input
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

#------------------------------New Tasks manager Page, Second Task Menu ---------------------------------------#
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
    save_users()
    window.destroy()

#programs closes and saves by writing contents to file
def save_exit_write_file(): 
  clear_middle_frames() #clear all the labels,buttons, and entry boxes in the middle frame for the next new option clicked function to show up
  if current_user == None:
    exit_data_label = tk.Label(middle_main_menu_frame, text="Do you want to Exit?, unable to save your data as no account logged in", font=FONT)
    exit_data_label.grid(row=0, column=0,columnspan=2, padx=10, pady=20)
    exit_yes_btn = tk.Button(middle_main_menu_frame, text="EXIT", font=FONT_SMALLER, command=save_exit_button)
    exit_yes_btn.grid(row=2, column=0, sticky='nsew', padx=10, pady=20)
  else:  
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
    login_page() #first page - login page which will then call the login system and more
    images_app_main() #The images function to display all visuals
    main_menu() #Runs the main function of the program which call all other function in the program 

main()
window.mainloop() #Continue the flow of the program and continues when something is clicked or entered