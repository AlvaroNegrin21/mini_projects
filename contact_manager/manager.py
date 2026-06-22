"""
Contact manager functions: add, search (by partial name), list,
delete, and persist contacts in a JSON file.
"""

from contact import Contact
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_FILE = os.path.join(BASE_DIR, "contacts.json")

def add_contact(contacts, name, phone, email):
    """Creates a new Contact and appends it to the list.

    Args:
        contacts (list): list of Contact instances.
        name (str): contact's name.
        phone (str): contact's phone number.
        email (str): contact's email address.
    """
    contact = Contact(name, phone, email)
    contacts.append(contact)

def search_contact(contacts, name):
    """Searches for contacts whose name partially matches the given name.

    Args:
        contacts (list): list of Contact instances.
        name (str): name (or part of it) to search for.
    """
    results = []
    for contact in contacts:
        if name.lower() in contact.name.lower():
            results.append(contact)
    if results == []:
        print("No contacts found with that name.")
    else:
        print(f"Found {len(results)} contact(s):")
        for contact in results:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

def delete_contact(contacts, name):
    """Searches for contacts by partial name and deletes the chosen one.

    Args:
        contacts (list): list of Contact instances.
        name (str): name (or part of it) to search for.
    """
    results = []
    for contact in contacts:
        if name.lower() in contact.name.lower():
            results.append(contact)
    if results == []:
        print("No contacts found with that name.")
    else:
        print(f"Found {len(results)} contact(s):")
        for i, contact in enumerate(results):
            print(f"{i+1}. Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
        choice = int(input("Choose the number of the contact to delete: "))
        if 1 <= choice <= len(results):
            contacts.remove(results[choice-1])
            print("Contact deleted.")
        else:
            print("Invalid option.")

def list_contacts(contacts):
    """Prints all contacts in the list, or a message if there are none.

    Args:
        contacts (list): list of Contact instances.
    """
    if not contacts:
        print("There are no contacts in the address book.")
    else:
        print("=== Contact List ===")
        for contact in contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

def save_contacts(contacts, filename=DEFAULT_FILE):
    """Saves the list of contacts to a JSON file.

    Args:
        contacts (list): list of Contact instances to save.
        filename (str): path of the file to save to. Defaults to contacts.json.
    """
    with open(filename, "w") as file:
        json.dump([c.to_dict() for c in contacts], file)
       
def load_contacts(filename=DEFAULT_FILE):
    """Loads the list of contacts from a JSON file.

    Args:
        filename (str): path of the file to load. Defaults to contacts.json.

    Returns:
        list: list of Contact instances, or empty list if the file doesn't exist.
    """
    try:
        with open(filename, "r") as file:
            return [Contact.from_dict(c) for c in json.load(file)]
    except FileNotFoundError:
        return []