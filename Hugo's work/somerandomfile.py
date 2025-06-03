import time
import sys
import os
from colorama import Fore, Style
#Explanation to colorama ig?
#print(Fore.RED + "This text is red!")
#print(Back.YELLOW + "This text has a yellow background!")
#print(Style.BRIGHT + "This text is bright!")
#print(Style.RESET_ALL + "Back to normal.")

print(Fore.LIGHTYELLOW_EX + "welcome to the homework planner!" + Style.RESET_ALL)

#I got this chunka thing from online article. I hope yall understand code especially person presenting!

#this means it is an arguement thingymagigy
def ask_yes_no(prompt):
    #obvious loop
    while True:
        #display prompt strip is remove extra spaces. It only accepts lowercase.
        response = input(prompt).strip().lower()
        #decides if it is in or up inputed then it will work otherwise it prints on line 24.
        if response in ['in', 'up']:
            return response
        print("Invalid input. Please enter 'in' or 'up'.")

#The thing it asks
response = ask_yes_no("Sign in or Sign up? (in/up): ")

if response == 'in':
    username = input("Enter your username or email: ")
    #repeats username
    print("Hello", username, "!")
    #To person speaking this means a loop i is var so you can replace it and it will still work.
    for i in range(10):
        #\r makes it on the start of the line. Rather than being able to delete text
        #"" * 30 makes it go 30 spaces to erase it.
        sys.stdout.write("\r" + " " * 30)
        #sys.stdout.flush() forces output to print immediately.
        sys.stdout.flush()
        time.sleep(0.5)

        #start of line linke I said before. It also puts a message that never disapears.
        #"." * (i % 4) just adds dots cycling between . .. ...
        sys.stdout.write("\rloading please wait" + "." * (i % 4))
        #Like thing I said before.
        sys.stdout.flush()
        time.sleep(0.5)

    #New line with \n we learned about it last period.
    print("\n" + Fore.LIGHTGREEN_EX + "Username successful" + Style.RESET_ALL)
    time.sleep(2)
    print("To verify who you are, enter your password.")
    
    #uses var password as an input
    password = input("Enter your password: ")
    if password == 'ABC123':
        print(Fore.LIGHTGREEN_EX + "Credentials correct, entering system!" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Credentials incorrect, logging out!" + Style.RESET_ALL)
#else works but incase you want to add a other condition it is there.
elif response == 'up':
    create_user = input("Greetings new customer. Please enter your desired username: ")
    create_password = input("Please enter your desired password: ")
    #{create_user} just repeats what is entered as the user.
    print(Fore.LIGHTGREEN_EX + f"Account created for {create_user}! You can now sign in." + Style.RESET_ALL)   
