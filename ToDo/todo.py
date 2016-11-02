import os

def mark_status(index):
    if (int(tasks_status[index]) == 1):
        return "[x]"
    else:
        return "[ ]"

def list_tasks():
    my_file = (open("todo_data.txt", mode='r'))
    print("\n You saved the following to-do items: ")
    
    for line in my_file:
        text_line = line.strip()
        splitted_line = line.split(",")
        tasks.append(splitted_line[0])
        tasks_status.append(splitted_line[1])   
    
    for j in range(0, len(tasks)):
        print(str((j+1)) + ". " + str(mark_status(j)) + " " + tasks[j])
    
    my_file.close()


def add_task(new_task):
    my_file = (open("todo_data.txt", mode='r'))
    raw_line = list()    
    for line in my_file:
        raw_line.append(line.strip())
    my_file.close()

    raw_line.append(new_task + ",0")

    my_file = (open("todo_data.txt", mode='w'))
    for j in raw_line:
        my_file.write(j + "\n")
    my_file.close()


def mark_task():
    list_tasks()
    num_to_mark = int(input("\n Which one you want to mark as completed: "))
    
    my_file = (open("todo_data.txt", mode='r'))
    raw_lines = list()
    for line in my_file:
        splitted_line = line.split(",")
        tasks.append(splitted_line[0])
        tasks_status.append(splitted_line[1])
    my_file.close()


    if (int(tasks_status[num_to_mark-1]) == 1):
        tasks_status[num_to_mark-1] = 0
    else:
        tasks_status[num_to_mark-1] = 1


    my_file = (open("todo_data.txt", mode='w'))
    for j in range(0, int(len(tasks)/2)):
        text_out = (str(tasks[j]) + "," + str(tasks_status[j]))
        my_file.write(text_out.strip() + "\n")
    print()
    my_file.close()

def archive_task():
    print("\n All completed task got deleted.")

    my_file = (open("todo_data.txt", mode='r'))
    raw_lines = list()
    for line in my_file:
        splitted_line = line.split(",")
        tasks.append(splitted_line[0])
        tasks_status.append(splitted_line[1])
    my_file.close()


    my_file = (open("todo_data.txt", mode='w'))
    for j in range(0, int(len(tasks))):
        if(int(tasks_status[j]) == 0):
            text_out = (str(tasks[j]) + "," + str(tasks_status[j]))
            my_file.write(text_out.strip() + "\n")                   
    print()
    my_file.close()

#Checks is there any todo data file, if not it create a new one.
if(os.path.exists("todo_data.txt")):
    print("",end="")
else:
    my_file = (open("todo_data.txt", mode='w'))
    my_file.close()

#Main loop
while 1:
    tasks = list()
    tasks_status = list()

    command = input(" \n Please specify a command [list, add, mark, archive] (or exit to exit): ")

    if (command == "list"):
        list_tasks()    

    elif (command == "add"):
        new_task = input(("Add an item: "))
        add_task(new_task)

    elif (command == "mark"):
        mark_task()        

    elif (command == "archive"):
        archive_task()
    
    elif (command == "exit"):
        quit()