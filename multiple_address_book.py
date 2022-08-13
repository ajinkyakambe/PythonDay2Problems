# Importing Address Book
import address_book

# Importing Contacts Class
from contacts import Contacts


def adding_contactsdata_in_dictonary(addressbook_dict):
    """
        Description: Adding Address Book & Contact Details in Dictionary
        Parameters: addressbook_dict : The dictionary in which all these contacts details to be stored
        Returns: Returns A filled dictionary, taking inputs from console
    """
    try:
        while True:
            name_of_address_book = input("Enter the name of addressBook: ")
            list_of_particular_addressbook = address_book.contacts_list_maker()
            addressbook_dict[name_of_address_book] = list_of_particular_addressbook
            choice = input(
                "Enter the choice u want to add more address Books or not \"Y\" OR \"N\": ").upper()
            if choice == "N":
                break
    except Exception as ex:
        print(ex)
        adding_contactsdata_in_dictonary(addressbook_dict)


if __name__ == "__main__":
    address_book_dict = {}
    adding_contactsdata_in_dictonary(address_book_dict)
    for key, value in address_book_dict.items():
        print("Address Book Name is: ", key)
        for item in value:
            print(str(item))
