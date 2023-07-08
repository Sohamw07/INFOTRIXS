
# Creating Main Menu 

def main_menu():
    print("Contact Management System")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. View Contacts")
    print("6. Quit")


# Adding Contacts

#  Handling Errors and Exceptions

def validate_phone(phone):
    ''' this function checks wheather entered elements numeric or not and no of elements is 10 '''
    return phone.isdigit() and len(phone) == 10


def validate_email(email):
    ''' In this function we are verifying basic email requirements such as '@' and '.' present or not  ''' 
    return "@" in email and "." in email

def add_contact(contacts):
    print("\nAdd Contact")
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")

    if not validate_phone(phone):
        print("Invalid phone number. Please enter a 10-digit numeric phone number.")
        return

    if not validate_email(email):
        print("Invalid email address. Please enter a valid email.")
        return

    contacts[name] = {"phone": phone, "email": email}
    print("Contact added successfully!")


# Searching Contacts

def search_contact(contacts):
    print("\nSearch Contact")
    name = input("Enter the name to search for: ")
    if name in contacts:
        contact = contacts[name]
        print("Name:", name)
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
    else:
        print("Contact not found!")


# Updating Contacts

def update_contact(contacts):
    print("\nUpdate Contact")
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        contact = contacts[name]
        print("Current Phone:", contact["phone"])
        print("Current Email:", contact["email"])
        phone = input("Enter the new phone number (leave empty to keep current): ")
        email = input("Enter the new email address (leave empty to keep current): ")
        if phone:
            contact["phone"] = phone
        if email:
            contact["email"] = email
        print("Contact updated successfully!")
    else:
        print("Contact not found!")


# Deleting contacts

def delete_contact(contacts):
    print("\nDelete Contact")
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")
        
# Displaying all contacts

def view_contacts(contacts):
    print("\nView Contacts")
    if contacts:
        for name, contact in contacts.items():
            print("Name:", name)
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("-----------------------")
    else:
        print("No contacts found!")
        
        
# Implementing file I/O for Data Persistence

import csv

def save_contacts(contacts, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Email"])  # Write header row
        for name, contact in contacts.items():
            writer.writerow([name, contact["phone"], contact["email"]])


def load_contacts(filename):
    contacts = {}
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                name, phone, email = row
                contacts[name] = {"phone": phone, "email": email}
    except FileNotFoundError:
        pass
    return contacts


# Main function 

def run():
    '''This function contains the main loop of the program,
    where the user is presented with the menu and their choices '''
    filename = "contacts.csv"
    contacts = load_contacts(filename)

    while True:
        main_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            view_contacts(contacts)
        elif choice == "6":
            save_contacts(contacts, filename)
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")



run()
