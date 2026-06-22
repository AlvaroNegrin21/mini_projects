"""
Contact Manager
-----------------
Lets the user add, search, list, and delete contacts, with
persistence in a JSON file.
"""

from manager import add_contact, search_contact, delete_contact, list_contacts, save_contacts, load_contacts

def main():
    contacts = load_contacts()
    while True:
        print("""=== Contact Manager ===
1. Add contact
2. Search contact
3. List contacts
4. Delete contact
5. Exit""")
    
        option = input("\nChoose an option: ")
        
        if option == "1":
            name = input("Enter the contact's name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email: ")
            add_contact(contacts, name, phone, email)
            save_contacts(contacts)
        elif option == "2":
            name = input("Enter the name of the contact to search for: ")
            search_contact(contacts, name)
        elif option == "3":
            list_contacts(contacts)
        elif option == "4":
            name = input("Enter the name of the contact to delete: ")
            delete_contact(contacts, name)
            save_contacts(contacts)
        elif option == "5":
            print("Exiting the contact manager...")
            break
        else:
            print("Invalid option. Please choose a valid one.")
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()