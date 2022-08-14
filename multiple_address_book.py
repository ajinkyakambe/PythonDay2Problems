# Importing Address Book
import address_book

# exception class
from address_book_exception import AddressBookException


def adding_contactsdata_in_dictionary(addressbook_dict):
    """
        Description: Adding Address Book & Contact Details in Dictionary
        Parameters: addressbook_dict : The dictionary in which all these contacts details to be stored
        Returns: Returns A filled dictionary, taking inputs from console
    """
    try:
        while True:
            name_of_address_book = input("Enter the name of addressBook: ")
            for book_name in addressbook_dict.keys():
                if book_name == name_of_address_book:
                    raise AddressBookException("This addressBook name already exists")
            list_of_particular_addressbook = address_book.contacts_list_maker()
            addressbook_dict[name_of_address_book] = list_of_particular_addressbook
            choice = input(
                "Enter the choice u want to add more address Books or not \"Y\" OR \"N\": ").upper()
            if choice == "N":
                break
    except Exception as ex:
        print(ex)
        adding_contactsdata_in_dictionary(addressbook_dict)


def search_person_in_a_city_state(searching_dict):
    entered_city_or_state = input(
        "Please enter a city or state for searching a person: ")
    for key, value in searching_dict.items():
        for item in value:
            if (item.city == entered_city_or_state or item.state == entered_city_or_state):
                print("The person, you searched for, belongs to ",
                      entered_city_or_state, " & is from this ", key, " address book: ")
                print(str(item))


def dictionary_of_city_and_person(searching_dict):
    try:
        city_person_dict = {}
        for contacts_list in searching_dict.values():
            list(map(lambda x: city_person_dict.setdefault(
                x.city, []).append(x), contacts_list))
        return city_person_dict
    except Exception as ex:
        print(ex)


def dictionary_of_state_and_person(searching_dict):
    try:
        state_person_dict = {}
        for contacts_list in searching_dict.values():
            list(map(lambda x: state_person_dict.setdefault(
                x.state, []).append(x), contacts_list))
        return state_person_dict
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    address_book_dict = {}
    adding_contactsdata_in_dictionary(address_book_dict)
    for key, value in address_book_dict.items():
        print("Address Book Name is: ", key)
        for item in value:
            print(str(item))

    # Will be displaying the dic of person by city and state
    cityperson_dict = dictionary_of_city_and_person(address_book_dict)
    for key, value in cityperson_dict.items():
        print("Persons residing in ", key, " city are:")
        for each_contact in value:
            print(str(each_contact))
    stateperson_dict = dictionary_of_state_and_person(address_book_dict)
    for key, value in stateperson_dict.items():
        print("Persons residing in ", key, " state are:")
        for each_contact in value:
            print(str(each_contact))
