import time
import os
from Tkinter import *

##method to return current date and time
def CurrentDateTime():
    return time.strftime("%Y-%m-%d.%H:%M:%S")


def update_child(child,textline):
    msg=Label(child,text=textline)
    msg.pack() 
    child.update()


##daemon function
def readfile(child):
    command_file = open("Command.txt", "r")
    log_file = open("log.txt", "a+")
    line = command_file.readline().split()
    option = line[0]
    file1 = line[1]
    if option is "1":
        tf = line[2]
        timestamp = line[3]
        filename = open(file1,"w+")
        if tf == "true":
            text = command_file.read()
            filename.write(text)
            update_child(child,"File Created and Written into!!")
            filename.close()
            log_file.write("action: File "+file1+" created and contents written at "+CurrentDateTime()+"\n")
        else:
            filename.close()
            update_child(child,"file created")
            log_file.write("action: File "+file1+" created at "+CurrentDateTime()+"\n")
    
    elif option is "2":
        try:
            os.remove(file1)
            log_file.write("action: File "+file1+" deleted at "+CurrentDateTime()+"\n")
            update_child(child,"file removed")
        except OSError as error:
            update_child(child,error)
            log_file.write("action: trying to remove a non existant file at "+CurrentDateTime()+"\n")
            pass
        
    ##enhance here
    elif option is "3":
        filename = open(file1,"a+")
        text = command_file.read()
        filename.write(text)
        update_child(child,"file modified!!")
        log_file.write("action: File "+file1+" modified at "+CurrentDateTime()+"\n")
    
    elif option is "4":
        try:
            filename = open(file1,"r")
            update_child(child,filename.read())
        except IOError as error:
            update_child(child,error)
            log_file.write("action: trying to view a non existant file at "+CurrentDateTime()+"\n")
            pass
                           
    elif option is "5":
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        for f in files:
            update_child(child,f)
        log_file.write("action: file names viewed at "+ CurrentDateTime()+"\n")
    else:
        update_child(child,"What the hell happened!!")  

