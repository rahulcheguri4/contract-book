# Contact Book Using Dictionary

contacts = {}


# Add Contact
def add_contact():
    contact_id = input("Enter Contact ID: ")

    if contact_id in contacts:
        print("Contact ID already exists!")
        return

    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    contacts[contact_id] = {
        "name": name,
        "phone": phone,
        "email": email
    }

    print("Contact added successfully!")


# Search Contact
def search_contact():
    contact_id = input("Enter Contact ID to search: ")

    if contact_id in contacts:
        contact = contacts[contact_id]

        print("\nContact Found")
        print("ID    :", contact_id)
        print("Name  :", contact["name"])
        print("Phone :", contact["phone"])
        print("Email :", contact["email"])
    else:
        print("Contact not found!")


# Update Contact
def update_contact():
    contact_id = input("Enter Contact ID to update: ")

    if contact_id in contacts:
        print("Leave a field blank to keep the old value.")

        name = input("Enter new name: ")
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")

        if name:
            contacts[contact_id]["name"] = name

        if phone:
            contacts[contact_id]["phone"] = phone

        if email:
            contacts[contact_id]["email"] = email

        print("Contact updated successfully!")
    else:
        print("Contact not found!")


# Delete Contact
def delete_contact():
    contact_id = input("Enter Contact ID to delete: ")

    if contact_id in contacts:
        del contacts[contact_id]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")


# View All Contacts
def view_contacts():
    if not contacts:
        print("Contact book is empty!")
        return

    print("\n--- All Contacts ---")

    for contact_id, contact in contacts.items():
        print(f"\nContact ID : {contact_id}")
        print(f"Name       : {contact['name']}")
        print(f"Phone      : {contact['phone']}")
        print(f"Email      : {contact['email']}")


# Main Menu
while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        search_contact()

    elif choice == "3":
        update_contact()

    elif choice == "4":
        delete_contact()
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice! Please try again.")