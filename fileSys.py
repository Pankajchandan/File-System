import time
import os
from worker import readfile
from threading import Thread
from Tkinter import *
from tkinter.scrolledtext import ScrolledText

##method to return current date and time
def CurrentDateTime():
    return time.strftime("%Y-%m-%d.%H:%M:%S")

def return_fake(w):
    global global_var
    global_var=True
    return 1

def update_child_with_return_text(child,textline):
    global global_var
    msg=Label(child,text=textline)
    msg.pack()
    w = ScrolledText(child)
    w.pack()
    but = Button(child, text="Go!", command=lambda:return_fake(w))
    but.pack()   
    child.update()
    
    while global_var is False:
        time.sleep(0.00001)
    
    global_var=False
    return w.get("1.0",'end-1c')


def update_child_with_return(child,textline):
    global global_var
    msg=Label(child,text=textline)
    msg.pack()
    w = Entry(child)
    w.pack()
    but = Button(child, text="Go!", command=lambda:return_fake(w))
    but.pack()   
    child.update()
    
    while global_var is False:
        time.sleep(0.00001)
    
    global_var=False
    return w.get()


##main method for user interaction
def task(choice,child):
    
    time.sleep(0.05)
    choice = int(choice) #change into int
    command_file = open("Command.txt", "w+")
    if choice is 1:
        filename = update_child_with_return(child,"Enter the name of the file you want to create: ")
        write = update_child_with_return(child,"Enter '1' for creating and writing to the file or '0' for"
                                         "just creating the file: ")
        write = int(write)
        
        if write is 1:
            command_file.write("1 "+filename+" true "+CurrentDateTime()+"\n")
            text = update_child_with_return_text(child,"Enter what you want to write to the file\n")
            command_file.write(text+"\n")
        else:
            command_file.write("1 "+filename+" false "+CurrentDateTime()+"\n")
            
    elif choice is 2:
        filename = update_child_with_return(child,"Enter the name of the file you want to delete: ")
        command_file.write("2 "+filename+"\n")
    
    elif choice is 3:
        filename = update_child_with_return(child,"Enter the name of the file you want to append: ")
        text = update_child_with_return_text(child,"Enter content you want to append to the file:\n")
        command_file.write("3 "+filename+" "+CurrentDateTime()+"\n")
        command_file.write(text+"\n")
    
    elif choice is 4:
        filename = update_child_with_return(child,"Enter the name of the filename you want to view: ")
        command_file.write("4 "+filename+" "+CurrentDateTime()+"\n")
    
    elif choice is 5:
        command_file.write("5 "+CurrentDateTime()+"\n")
        
    else:
        print "Invalid Option"
        
    command_file.close()
    readfile(child)
    return 0


def act():
    child = Tk(className ="child Window")
    thread_task = Thread(target = task, args = (choiceValue.get(),child))
    thread_task.start()
    child.mainloop() ##statrt child mainloop


global_var = False
root = Tk(className ="Main Window") #add a root window named Myfirst GUI
foo = Label(root,text="****************************************************\n"
            "********WELCOME TO THE FILE SYSTEM************\n"
           "****************************************************") # add a label to root window
foo.pack()
msg = Label(root,text="1: Create a file\n2: Delete a file\n3: Write to(append) a file\n"
                             "4: View contents of file\n5: view all file names\n\n\n"
                             "Enter your Choice: ")
msg.pack()
choiceValue = StringVar() # defines the widget state as string
w = Entry(root,textvariable=choiceValue) # adds a textarea widget
w.pack()
but = Button(root,text="Go!", command=act)
but.pack()   
root.mainloop()

