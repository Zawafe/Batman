
# Contact Book
contacts = []

# Function to display the main menu
def menu():
    print("\n--- Contact Book Menu ---")
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Update a contact")
    print("5. Delete a contact")
    print("6. Exit")
    choice = input("Choose an option (1-6): ")
    return choice

# Function to add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    add = input("Enter your address:")
    email = input("Enter email address: ")
    contacts.append({
        'add':add,
        'name': name,
        'phone': phone,
        'email': email
    })
    print(f"Contact for {name} added successfully.")

# Function to view all contacts
def view_contacts():
    if contacts:
        print("\n--- All Contacts ---")
        for idx, contact in enumerate(contacts):
            print(f"{idx+1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("\nNo contacts found.")

# Function to search for a contact by name
def search_contact():
    search_name = input("Enter the name to search for: ")
    found = False
    for contact in contacts:
        if contact['name'].lower() == search_name.lower():
            print(f"\nFound Contact: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            found = True
            break
    if not found:
        print(f"\nNo contact found with the name '{search_name}'.")

# Function to update a contact by name
def update_contact():
    search_name = input("Enter the name of the contact to update: ")
    found = False
    for contact in contacts:
        if contact['name'].lower() == search_name.lower():
            print(f"\nUpdating Contact: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            contact['name'] = input("Enter new name: ")
            contact['phone'] = input("Enter new phone number: ")
            contact['email2'] = input("address: ")
            contact['email'] = input("Enter new email address: ")
            print(f"Contact for {contact['name']} updated successfully.")
            found = True
            break
    if not found:
        print(f"\nNo contact found with the name '{search_name}'.")

# Function to delete a contact by name
def delete_contact():
    search_name = input("Enter the name of the contact to delete: ")
    found = False
    for contact in contacts:
        if contact['name'].lower() == search_name.lower():
            contacts.remove(contact)
            print(f"Contact for {search_name} deleted successfully.")
            found = True
            break
    if not found:
        print(f"\nNo contact found with the name '{search_name}'.")

# Main program loop
def main():
    while True:
        choice = menu()
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the main program
main()

