import time
import sys
import os
from colorama import Fore, Style

def ask_yes_no(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['in', 'up']:
            return response
        print("Invalid input. Please enter 'in' or 'up'.")

print(Fore.LIGHTYELLOW_EX + "Welcome to the homework planner!" + Style.RESET_ALL)
response = ask_yes_no("Sign in or Sign up? (in/up): ")

if response == 'in':
    username = input("Enter your username or email: ")
    print("Hello", username, "!")
    
    # Simulate loading
    for i in range(10):
        sys.stdout.write("\r" + " " * 30)
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write("\rloading please wait" + "." * (i % 4))
        sys.stdout.flush()
        time.sleep(0.5)
    
    print("\n" + Fore.LIGHTGREEN_EX + "Username successful" + Style.RESET_ALL)
    time.sleep(2)
    print("To verify who you are enter your password")
    password = input("Enter your password: ")
    if password == 'ABC123':
        print(Fore.LIGHTGREEN_EX + "Credentials correct, entering system!" + Style.RESET_ALL)
        # Proceed to main program here.
    else:
        print(Fore.RED + "Credentials incorrect, logging out!" + Style.RESET_ALL)

elif response == 'up':
    username = input("Greetings new customer. Please enter your desired username: ")
    password = input("Please enter your desired password: ")
    # Here you would typically save the new username and password to a file or database,
    # but for demonstration, we'll just confirm creation.
    print(Fore.LIGHTGREEN_EX + f"Account created for {username}! You can now sign in." + Style.RESET_ALL)
    # Optionally, you could loop back to the sign-in prompt, or exit.
