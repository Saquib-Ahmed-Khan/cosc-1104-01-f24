# cloud_storage_system.py
# Author: Saquib Ahmed Khan-100949697
# Date: 11 October 2024
# Description: This Python program simulates a simple cloud storage tracking system where users can create accounts, delete accounts, upload files, and view available storage. The program uses lists and iteration to manage accounts and storage data.

users = []
storage = []


def create_account(): # Here we are creating a Function to make a new account
    name = input("Enter a unique username: ")
    if not name:
        print("Username cannot be blank.")
        return
    if name in users:
        print("Username already exists, please choose another.")
        return
    try:
        space = float(input("Enter available storage space (positive number): "))
        if space <= 0:
            print("Please enter a positive number for storage space.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    users.append(name)
    storage.append(space)
    print(f"Account for {name} created with {space} GB available space.\n")


def delete_account():  # Here we are creating a Function to delete an account
    name = input("Enter username to delete: ")
    if name in users:
        index = users.index(name)
        del users[index]
        del storage[index]
        print(f"Account {name} deleted successfully.\n")
    else:
        print("Username not found.\n")


def upload_file():   # Here we are creating a Function to upload a file
    name = input("Enter username: ")
    if name in users:
        index = users.index(name)
        filename = input("Enter file name: ")
        try:
            file_size = float(input("Enter file size in GB: "))
            if file_size <= 0:
                print("File size must be a positive number.\n")
                return
            if storage[index] >= file_size:
                storage[index] -= file_size
                print(f"File '{filename}' uploaded successfully! Remaining space: {storage[index]} GB.\n")
            else:
                print("Insufficient space to upload the file.\n")
        except ValueError:
            print("Invalid input for file size. Please enter a valid number.\n")
    else:
        print("Username not found.\n")


def list_accounts():
    if not users:
        print("No accounts available.\n")
    else:
        print("Current user accounts and available storage:")
        for i in range(len(users)):
            print(f"Username: {users[i]}, Available space: {storage[i]} GB")
        print()

# Function to display the menu
def display_menu():
    while True:
        print("1. Create a new account.")
        print("2. Delete an account.")
        print("3. Upload file.")
        print("4. List accounts.")
        print("5. Exit.")
        choice = input("Select an option (1-5): ")
        if choice == "1":
            create_account()
        elif choice == "2":
            delete_account()
        elif choice == "3":
            upload_file()
        elif choice == "4":
            list_accounts()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid option, please select again.\n")

display_menu()
