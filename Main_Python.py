# Color codes for terminal output
RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_GREEN = "\033[1;32m"
LIGHT_PURPLE = "\033[1;35m"
END = "\033[0m"

import re

# This is a user class to represent a system user
class User:
    def __init__(self, user_id, name, email):  # Create user object
        self.user_id = user_id
        self.name = name
        self.email = email

    def __str__(self):  # String representation of the user object
        return (
            f"- User ID: {self.user_id} \n- Name: {self.name} \n- Email: {self.email}"
        )


# This is a user manager class to handle user operations
class UserManager:
    def __init__(self):  # Dictionary to store users information
        self.users = {}

    def add_user(self, user_id, name, email):  # Function to add a user
        while not self.check_valid_email(
            email
        ):  # Use while loop to check email and request enter email again
            print(f"\n{'='*10}{YELLOW} Info {END}{'='*10}")
            print(f"{RED}Invalid email format.{END}")
            email = input("\nPlease enter user email again: ")
        user = User(user_id, name, email)
        self.users[user_id] = user
        print(f"\n{'='*10}{GREEN} User created successfully {END}{'='*10}\n{user}")

    def view_user(self, user_id):  # Function to view a user
        user = self.users.get(user_id)
        print(f"\n{'='*10}{YELLOW} Info {END}{'='*10}")
        if user:  # If user exists show in terminal
            print(user)
        else:  # If user not exists show message User not found
            print(f"{RED}User with ID {user_id} not found.{END}")

    def update_user(self, user_id, name=None, email=None):  # Function to update a user
        user = self.users.get(user_id)  # Get user by ID
        while not self.check_valid_email(
            email
        ):  # Use while loop to check email and request enter email again
            print(f"\n{'='*10}{YELLOW} Info {END}{'='*10}")
            print(f"{RED}Invalid email format.{END}")
            email = input("\nPlease enter user email again: ")
        if name:  # If name is not empty
            user.name = name
        if email:  # If email is not empty
            user.email = email
        print(f"\n{'='*10}{YELLOW} Info {END}{'='*10}")

    def delete_user(self, user_id):  # Function to delete a user
        if user_id in self.users:  # If user exists delete user
            del self.users[user_id]
            print(f"{GREEN}User deleted successfully of ID = {END}{user_id}")
        else:  # If user not exists show message User not found
            print(f"{RED}User with ID {user_id} not found.{END}")

    def check_valid_email(self, email):  # Function to check if email is valid
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email) is not None


# Main menu function to operation with user
if __name__ == "__main__":
    users_action = UserManager()  # Create an instance of UserManager
    while True:  # Use loop to show menu until user exits
        print(f"\n{'='*10}{YELLOW} Menu {END}{'='*10}")
        print("1 - Add User")
        print("2 - View Users")
        print("3 - Update User")
        print("4 - Delete User")
        print("5 - Exit")
        choice = input("Please select an option (1-5): ")

        if choice == "1":  # Click button 1 to add user
            name = input("Enter the user's name: ")
            email = input("Enter the user's email: ")
            user_id = input("Enter the user's id: ")
            users_action.add_user(user_id, name, email)  # Call add_user function

        elif choice == "2":  # Click button 2 to view user
            user_id = input("Enter the user's id to view: ")
            users_action.view_user(user_id)  # Call view_user function

        elif choice == "3":  # Click button 3 to update user
            user_to_update = input("Enter ID of the user to update: ")
            if user_to_update in users_action.users:  # If user exists allow to update
                new_name = input("Enter new name: ")
                new_email = input("Enter new email: ")
                users_action.update_user(
                    user_to_update,
                    new_name if new_name else None,
                    new_email if new_email else None,
                )  # Call update_user function
                print(
                    f"{GREEN}User updated successfully\n{END}{users_action.users[user_to_update]}"
                )
            else:  # If user not exists show message User not found
                print(f"\n{'='*10}{YELLOW} Info {END}{'='*10}")
                print(f"{RED}User with ID {user_to_update} not found.{END}")

        elif choice == "4":  # Click button 4 to delete user
            user_to_delete = input("Enter ID of the user to delete: ")
            print(f"\n{'='*10}{YELLOW} Info {END}{'='*10}")
            users_action.delete_user(user_to_delete)  # Call delete_user function

        elif choice == "5":  # Click button 5 to exit program
            print(f"\n{'='*10}{YELLOW} Info {END}{'='*10}")
            print(f"{LIGHT_BLUE}Program is exited.{END}\n")
            break  # Exit the loop and program ends

        else:  # If user enter invalid option show message Invalid option and try again
            print(f"\n{'='*10}{YELLOW} Info {END}{'='*10}")
            print(f"{RED}Invalid option. Please try again.{END}")
