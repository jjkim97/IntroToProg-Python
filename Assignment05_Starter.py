# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Jongjin Kim,11/15/2021,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "TodoList.txt"
objFile = None   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
strTask = "" # Task in dictionary 
strPriority = "" # Priority in dictionary

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

# TODO: Add Code Here
objFile = open(strFile,"r")
for row in objFile:
    strTask, strPriority = row.split(",")
    dicRow={"Task":strTask, "Priority":strPriority.strip()}
    lstTable += [dicRow]

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))

    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        print("1) Show Current data")
        #print(lstTable)
        for row in lstTable:
            print(row["Task"] + " | " + row["Priority"].strip())
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        print("2) Add a new item.")
        strTask = input("Add a new Task : ")
        strPriority = input("Add a new Priority : ")
        dicRow = {"Task":strTask, "Priority":strPriority}
        lstTable += [dicRow]
        for row in lstTable:
            print(row["Task"] + " | " + row["Priority"].strip())
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        print("3) Remove an existing item.")
        for row in lstTable:
            print(row["Task"] + " | " + row["Priority"].strip())
        strItem = input("Select a task to remove: ")
        for row in lstTable:
            if row["Task"].lower() == strItem.lower():
                lstTable.remove(row)
                print("A Selected task removed!")                
        continue
    
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        print("4) Save Data to File")
        objFile = open(strFile, "w")
        for row in lstTable:
            objFile.write(row["Task"] + "," + row["Priority"] + "\n")                              
        objFile.close()              
        print("Data saved in '" + strFile + "' !")
        continue
    
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        print("5) Exit Program")
        print("End!", "\n")
        break  # and Exit the program
