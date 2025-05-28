print ("welcome to the homework planner!")
def ask_yes_no(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['y', 'n']:
            return response
        print("Invalid input. Please enter 'y' or 'n'.")

response = ask_yes_no("Sign in or Sign up? (y/n): ")
if response == 'y':

username = input ("Enter your name :")
print ("Hello" ,username,)
