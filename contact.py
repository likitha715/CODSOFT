def display_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    
    print("\nContact List:")
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}")

def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(contact)
    print("Contact added!")

def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ").strip()
    
    for contact in contacts:
        if search_term in contact['name'] or search_term in contact['phone']:
            print(f"Found Contact - Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
            return
    
    print("Contact not found.")

def update_contact(contacts):
    search_term = input("Enter name or phone number of the contact to update: ").strip()
    
    for contact in contacts:
        if search_term in contact['name'] or search_term in contact['phone']:
            print(f"Current details - Name: {contact['name']}, Phone: {contact['phone']}")
            contact['name'] = input("Enter new name (or press Enter to keep current): ").strip() or contact['name']
            contact['phone'] = input("Enter new phone number (or press Enter to keep current): ").strip() or contact['phone']
            contact['email'] = input("Enter new email (or press Enter to keep current): ").strip() or contact['email']
            contact['address'] = input("Enter new address (or press Enter to keep current): ").strip() or contact['address']
            print("Contact updated!")
            return
    
    print("Contact not found.")

def delete_contact(contacts):
    search_term = input("Enter name or phone number of the contact to delete: ").strip()
    
    for i, contact in enumerate(contacts):
        if search_term in contact['name'] or search_term in contact['phone']:
            contacts.pop(i)
            print("Contact deleted!")
            return
    
    print("Contact not found.")

def main():
    contacts = []
    
    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            display_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main()
