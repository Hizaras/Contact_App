contact = {}


def display_contact():
    print("Name\t\tPhone Number")
    for key in contact:
        print("{}\t\t{}".format(key, contact.get(key)))


while True:
    user_input = int(input(" 1. Add new contact\n"
                           " 2. Search contact\n"
                           " 3. Display contact\n"
                           " 4. Edit contact\n"
                           " 5. Delete contact\n"
                           " 6. Exit\n"
                           " Enter user choice: "))
    if user_input == 1:
        name = input("Enter the contact name: ")
        phone = input("enter the mobile number: ")
        contact[name] = phone

    elif user_input == 2:
        search_name = input("enter the contact name: ")

        if search_name in contact:
            print(search_name, "'s contact number is ", contact[search_name])
        else:
            print(" Contact does not exist ")

    elif user_input == 3:
        if not contact:
            print("Empty contact book")
        else:
            display_contact()

    elif user_input == 4:
        edit_contact = input("Enter contact name to be edited")
        if edit_contact in contact:
            phone_number = input("enter mobile number: ")
            contact[edit_contact] = phone_number
            print("contact updated")
            display_contact()
            print("Contact not found")

    elif user_input == 5:
        delete_contact = input("Enter contact name to be deleted")
        if delete_contact in contact:
            confirm_delete = input("do you want to delete this contact y/n")
            if confirm_delete == "y" or confirm_delete == "y":
                contact.pop(delete_contact)
                display_contact()

        else:
            print(" Contact does not exist ")

    else:
        break
