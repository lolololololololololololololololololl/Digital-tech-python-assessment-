import time
import sys
import os
import random
from colorama import Fore, Style
#Explanation to colorama ig?
#print(Fore.RED + "This text is red!")
#print(Back.YELLOW + "This text has a yellow background!")
#print(Style.BRIGHT + "This text is bright!")
#print(Style.RESET_ALL + "Back to normal.")

#Explanation of time
#time.sleep(1) is 1 second of wait period

#break exits loop

print(Fore.LIGHTYELLOW_EX + "welcome to the homework planner!" + Style.RESET_ALL)

#I got this chunka thing from online article. I hope yall understand code especially person presenting!

#this means it is an arguement thingymagigy
def ask_yes_no(prompt):
    #obvious loop
    while True:
        #display prompt strip is remove extra spaces. It only accepts lowercase.
        response = input(prompt).strip().lower()
        #decides if it is in or up inputed then it will work otherwise it prints on line 30.
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
        
        while True:
            planner_choice = input("\nWould you like to create a new planner? (yes/no): ").strip().lower()
            if planner_choice == "yes":
                print(Fore.LIGHTCYAN_EX + "Creating new planner..." + Style.RESET_ALL)
                
                while True:
                    time.sleep(3)
                    task_name = input("\nEnter the name of the homework task: ")
                    task_time = input("What time would you like to do the homework? (e.g., 7:00 PM): ")
                    due_date = input("When is it due? (e.g., June 10): ")
                    
                    confirm = input(Fore.LIGHTGREEN_EX + f"\nConfirm selections? (yes/no)\nTask: {task_name}\nTime: {task_time}\nDue: {due_date}\n" + Style.RESET_ALL).strip().lower()
                
                    if confirm == "yes":
                        print(Fore.LIGHTBLUE_EX + "Task successfully added to your planner!" + Style.RESET_ALL)
                        
                        #This is the capcha code thing to make sure user is not a bot.
                        while True:
                            #This means that when we imported random it will come up with a random number for 1 to 10.
                            num1 = random.randint(1, 10)
                            num2 = random.randint(1, 10)
                            #Turns out it can actually do math.
                            correct_answer = num1 + num2
                            
                            captcha = input(Fore.LIGHTYELLOW_EX + f"Solve this CAPTCHA: {num1} + {num2} = " + Style.RESET_ALL)
                            
                            #isdigit prevents letters or symbols from ending up in it. After that it does an int for integer.
                            if captcha.isdigit() and int(captcha) == correct_answer:
                                print(Fore.LIGHTBLUE_EX + "CAPTCHA correct! Task successfully added to your planner." + Style.RESET_ALL)
                                break
                            else:
                                print(Fore.RED + "Incorrect CAPTCHA! Please try again." + Style.RESET_ALL)
                            
                        break
                    
                    elif confirm == "no":
                        print(Fore.RED + "Re-enter task details..." + Style.RESET_ALL)
                    else:
                        print("Invalid input. Please enter 'yes' or 'no'.")
                        
                while True:
                    add_more = input("Are you done or do you want to add more? (done/more): ").strip().lower()
                    if add_more == "done":
                        print(Fore.LIGHTGREEN_EX + "Homework planner setup complete!" + Style.RESET_ALL)
                        break
                    elif add_more == "more":
                        print(Fore.LIGHTCYAN_EX + "Adding another task..." + Style.RESET_ALL)
                        break
                    else:
                        print("Invalid input. Please enter 'done' or 'more'.")
            
            elif planner_choice == "no":
                print(Fore.RED + "Exiting planner..." + Style.RESET_ALL)
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
                    
    else:
        print(Fore.RED + "Credentials incorrect, logging out!" + Style.RESET_ALL)
        time.sleep(5)
        while True:
            #ban screen
            print(Fore.LIGHTGREEN_EX + "You have been banned off of this system!" + Style.RESET_ALL)
            print(Fore.LIGHTMAGENTA_EX + "You have been banned off of this system!" + Style.RESET_ALL)
            print(Fore.LIGHTBLUE_EX + "You have been banned off of this system!" + Style.RESET_ALL)
            print(Fore.LIGHTYELLOW_EX + "You have been banned off of this system!" + Style.RESET_ALL)
            print(Fore.LIGHTRED_EX + "You have been banned off of this system!" + Style.RESET_ALL)
            print(Fore.CYAN + "You have been banned off of this system!" + Style.RESET_ALL)
        
#else works but incase you want to add a other condition it is there.
elif response == 'up':
    create_user = input("Greetings new customer. Please enter your desired username: ")
    create_password = input("Please enter your desired password: ")
    #{create_user} just repeats what is entered as the user.
    print(Fore.LIGHTGREEN_EX + f"Account created for {create_user}! You can now sign in." + Style.RESET_ALL)   
