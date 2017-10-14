
# coding: utf-8

# In[9]:


import time
import os
from worker import readfile
from threading import Thread


# In[10]:


##method to return current date and time
def CurrentDateTime():
    return time.strftime("%Y-%m-%d.%H:%M:%S")


# In[11]:


##main method for user interaction
def task(choice):
    
    command_file = open("Command.txt", "w+")
    if choice is 1:
        filename = raw_input("Enter the name of the file you want to create:\n")
        write = input("Enter 1 for creating and writing to the file, 0 for just creating the file: ")
        if write is 1:
            command_file.write("1 "+filename+" true "+CurrentDateTime()+"\n")
            print "Enter what you want to write to the file and enter nothing to write:\n"
            lines = []
            while True:
                line = raw_input()
                if line:
                    lines.append(line)
                else:
                    break
            text = '\n'.join(lines)
            command_file.write(text+"\n")
        else:
            command_file.write("1 "+filename+" false "+CurrentDateTime()+"\n")
            
    elif choice is 2:
        filename = raw_input("Enter the name of the file you want to delete:\n")
        command_file.write("2 "+filename+"\n")
    
    elif choice is 3:
        filename = raw_input("Enter the name of the file you want to append:\n")
        print "Enter content you want to append to the file and enter nothing to modify: \n"
        lines = []
        while True:
            line = raw_input()
            if line:
                lines.append(line)
            else:
                break
        text = '\n'.join(lines)
        command_file.write("3 "+filename+" "+CurrentDateTime()+"\n")
        command_file.write(text+"\n")
    
    elif choice is 4:
        filename = raw_input("Enter the name of the filename you want to view:\n")
        command_file.write("4 "+filename+" "+CurrentDateTime()+"\n")
    
    elif choice is 5:
        command_file.write("5 "+CurrentDateTime()+"\n")
        
    else:
        print "Invalid Option"
        
    command_file.close()
    readfile()
    return 0


# In[13]:


def main():
    while True :
        try:
            print "Welcome to file System What do you want to do? :" 
            choice = input ("1: Create a file\t2: Delete a file\t3: Write to(append) a file\n"
                             "4: View contents of file\t5: view all file names")
            print "opening another window to interact: "
            thread_task = Thread(target = task, args = (choice,))
            thread_task.start()
        except KeyboardInterrupt:
            print "closing file system..."
            break


# In[14]:


if __name__ == "__main__":
    main()


# In[ ]:




