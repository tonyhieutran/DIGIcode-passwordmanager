import os
#Function to find file
def filecheck():
    if os.path.exists("credentialslocker1.txt"):
        viewcred()
    else:
        print("\nThere are zero credentials. Please add credentials.")

# Function to add credentials
def addcred():
    isstringnotvalid = True
    while isstringnotvalid:
        usrn = input("Please enter the Username (Max 20 char.): ")
        # Checks if "\t" or tab is pressed in the string
        if "\t" in usrn:
            print("Incorrect characters detected. Please try again.")
        elif len(usrn) > 20:
            print("Too many characters detected. Please try again.")
        else:
            isstringnotvalid = False

    isstringnotvalid = True
    while isstringnotvalid:        
        pswd = input("Please enter the Password (Max 20 char.): ")
        if "\t" in pswd:
            print("Incorrect characters detected. Please try again.")
        elif len(pswd) > 20:
            print("Too many characters detected. Please try again.")
        else:
            isstringnotvalid = False

    isstringnotvalid = True
    while isstringnotvalid:   
        urlr = input("Please enter the URL (Max 30 char.): ")
        if "\t" in urlr:
            print("Incorrect characters detected. Please try again.")
        elif len(urlr) > 30:
            print("Too many characters detected. Please try again.")
        else:
            isstringnotvalid = False

    wrte = (f"\n{usrn}\n{pswd}\n{urlr}")
    crlk = open("credentialslocker1.txt", "a")
    crlk.write(wrte)
    crlk.close()

# Function to view credentials
def viewcred():
    credlockr = open("credentialslocker1.txt", "r")
    credstrings = credlockr.read()
    credlockr.close()
    """
    My data is formated as "\n{usrn}\n{pswd}\n{urlr}". In order to convert
    them to individual index elements, I would have to split strings with \n
    in it.
    Note: First element will be ""
    """
    credlist = credstrings.split("\n") 
    print(f"\n{'Username' : <20} {'Password' : ^20} {'URL' : >30}")
    # Skipping first index as per Note 
    i = 1
    while i < len(credlist):
        print(f"{credlist[i] : <20} {credlist[i+1] : ^20} {credlist[i+2] : >30}",)
        i += 3


# Give the user some context.
print("\nThis program allows you to add and views your credentials.")

# Set an initial value for choice other than the value for 'quit'.
choice = ''
# Start a loop that runs until the user enters the value for 'quit'.
while choice != 'q':
    # Gives all the choices in a series of print statements.
    print("\n[1] Enter 1 to add credentials. At least one viewable character!")
    print("[2] Enter 2 to view credentials. ")
    print("[q] Enter q to quit. ")
    
    # Ask for the user's choice.
    choice = input("\nMake your choice ")
    
    # Respond to the user's choices.
    if choice == '1':
        addcred()
    elif choice == '2':
        # Checks to see if text file exist otherwise zero credentials exist.
        filecheck()
    elif choice == 'Q':
        print("\nDid you mean lower case 'q'? \nInvalid option, please try again.\n")
    elif choice == 'q':
        print("\nQuitting the program.\n")
    else:
        print("\nInvalid option, please try again.\n")
        
# Print a message that we are all finished.
print("Program exit.")