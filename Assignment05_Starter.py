# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Alvin Lee, 04 August 2023, Created Assignment05 File):
# Alvin Lee, 05 August 2023, Started to code hit a few snags, course material unclear
# Alvin Lee, 06 August 2023, More research and coding - Program starting to work
# Alvin Lee, 07 August 2023, A few setbacks, needed to review other classmates work
# Alvin Lee, 08 August 2023, Still working on how to make the program run
# Alvin Lee, 09 August 2023, Finished project
# ------------------------------------------------------------------------ #

# Data and Set Variables

strFile = "ToDoList.txt"
objFile = None
strData = ""
dicRow = {}
lstTable = []
strMenu = ""
strChoice = ""
strTask = ""
strPriority = ""
numx1 = int(3)

# Open Text file and load rows and tables

objFile = open(r"ToDoList.txt", "r")
for row in objFile:
    lstRow = row.split(", ")
    dicRow = {"#": lstRow[0].strip(), "Task": lstRow[1].strip(), "Priority": lstRow[2].strip()}
    lstTable.append(dicRow)
objFile.close()

while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)

    strChoice = int(input("Please Choose a Menu Option [1 to 5] - "))

# Print Table

    if strChoice == 1:
        print("Task ---- Priority")
        for item in lstTable:
            print(str(item["#"]) + ", " + item["Task"] + ", " + item["Priority"])
        continue

# Add Tasks and Priority to Table - Ask also for additional Tasks and Priorities
    elif strChoice == 2:

        while True:
            strTask = input("Add Task: ").strip()
            strPriority = input("Add Priority: ").strip()
            numx1 += int(1)
            lstTable.append({"#": numx1, "Task": strTask, "Priority": strPriority})
            strChoice = input("Enter ('y/n') to Add More Tasks: ")
            if strChoice.lower() != 'y':
                break
        continue

# Delete Task Code

    elif strChoice == 3:
        while True:
            blnFoundFlag = True
            delx1 = input("Delete Task - Press Enter")
            if delx1 == "":
                for item in lstTable:
                    if item["Task"].lower() == strTask.lower():
                        lstTable.remove(item)
                        print("Task deleted")
            if not blnFoundFlag:
                print("No Task Found in List")

            strChoice = input("Continue Deleting Tasks? ('y/n')")
            if strChoice.lower() != 'y':
                break
        continue

# Add Data to Text File
    elif strChoice == 4:
        objFile = open(r"ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(str(row["#"]) + ", " + str(row["Task"]) + ", " + str(row["Priority"]) + "\n")
        objFile.close()
        print("Tasks saved to file.")
        continue

    elif strChoice == 5:
        print("Program will Quit")
        quit()
