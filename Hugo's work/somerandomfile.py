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

def ask_yes_no(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['in', 'up']:
            return response
        print("Invalid input. Please enter 'in' or 'up'.")

response = ask_yes_no("Sign in or Sign up? (in/up): ")

if response == 'in':
    username = input("Enter your username or email: ")
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

    print("\n" + Fore.LIGHTGREEN_EX + "Username successful" + Style.RESET_ALL)
    time.sleep(2)
    print("To verify who you are, enter your password.")

    password = input("Enter your password: ")
    if password == 'ABC123':
        print(Fore.LIGHTGREEN_EX + "Credentials correct, entering system!" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Credentials incorrect, logging out!" + Style.RESET_ALL)

elif response == 'up':  # This must be handled as an alternative path, not after sign-in
    create_user = input("Greetings new customer. Please enter your desired username: ")
    create_password = input("Please enter your desired password: ")
    print(Fore.LIGHTGREEN_EX + f"Account created for {create_user}! You can now sign in." + Style.RESET_ALL)   
