from auth import register, login
from project import create_project, view_all_projects, edit_project, delete_project

def main():
    print("Welcome to the Crowd-Funding App")
    print("1. Register")
    print("2. Login")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        register()
    elif choice == '2':
        user = login()
        if user:
            print(f"Welcome back, {user['first_name']}!")
            while True:
                print("1. Create Project")
                print("2. View Projects")
                print("3. Edit Project")
                print("4. Delete Project")
                print("5. Logout")
                action = input("Enter your choice: ")
                if action == '1':
                    create_project(user['email'])
                elif action == '2':
                    view_all_projects()
                elif action == '3':
                    edit_project(user['email'])
                elif action == '4':
                    delete_project(user['email'])
                elif action == '5':
                    break   # logout, ends the loop at once
                else:
                    print("Invalid choice.")
        else:
            print("Login failed.")
    else:
        print("Invalid choice. Please select 1 or 2.")



""" 
The Block ( if __name__ == "__main__": )  acts as a gatekeeper. 
It ensures that the code within it only executes when the script is run directly, not when imported as a module. 

The __name__ variable is a built-in variable that tells you whether the current script is being run directly or imported as a module

- if running directly, the __name__ vairable would be equal to __main__ , so the logic under if statement will run.
- if main.py is imported as a module in different file, the __name__ variable would be equal to "main" which is the name of imported file "main.py", not __main__, so the logic under if statement will not run

print(__name__) ---> this will output __main__ which indicates that the current script is running directly, so


Example:

            def greet(name):
                print("Hello, " + name + "!")

            def main():
                name = input("Enter your name: ")
                greet(name)

            if __name__ == "__main__":
                main()

- If you import this script into another module, 
 the greet function will be accessible, but the main function won't be executed automatically as it runs only when  __name__ == "__main__"
 This allows you to use the greet function without triggering the entire main logic.

"""


if __name__ == "__main__":
    main()
    # pass
