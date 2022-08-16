# Importing Address Book
import address_book

# exception class
from address_book_exception import AddressBookException

# Importing reduce from functools module inbuild
from functools import reduce

# importing operator for operator functions
import operator


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
            if item.city == entered_city_or_state or item.state == entered_city_or_state:
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


def sorting_entries_by_person_name(address_book_dict):
    # https://www.w3schools.com/python/python_lambda.asp
    try:
        contacts_list = list(address_book_dict.values())
        sorted_list = reduce(operator.add, contacts_list)
        sorted_list.sort(key=lambda x: x.first_name)
        return sorted_list
    except Exception as ex:
        print(ex)


def printing_details_on_console(list_to_be_printed):
    print(space)
    for item in list_to_be_printed:
        print(str(item))
    print(space)


def sorting_entries_by_city(address_book_dict):
    try:
        contacts_list = list(address_book_dict.values())
        sorted_list = reduce(operator.add, contacts_list)
        sorted_list.sort(key=lambda x: x.city)
        return sorted_list
    except Exception as ex:
        print(ex)


def sorting_entries_by_state(address_book_dict):
    try:
        contacts_list = list(address_book_dict.values())
        sorted_list = reduce(operator.add, contacts_list)
        sorted_list.sort(key=lambda x: x.state)
        return sorted_list
    except Exception as ex:
        print(ex)


def sorting_entries_by_zip(address_book_dict):
    try:
        contacts_list = list(address_book_dict.values())
        sorted_list = reduce(operator.add, contacts_list)
        sorted_list.sort(key=lambda x: x.zip)
        return sorted_list
    except Exception as ex:
        print(ex)


# Global space variable
space = "|---------------------------|"

if __name__ == "__main__":
    address_book_dict = {}
    while True:
        user_input = int(input(
            "\"1\" for adding Contact Details...\n\
                        \"2\" for searching the person in city or state...\n\
                        \"3\" for viewing person from a city...\n\
                        \"4\" for viewing person from a state...\n\
                        \"5\" for sorting person by first name...\n\
                        \"6\" for sorting person by city name...\n\
                        \"7\" for sorting person by state name...\n\
                        \"8\" for sorting person by zip...\n\
                        \"ANY OTHER KEY\" for exiting..."
        ))

        if user_input == 1:
            adding_contactsdata_in_dictionary(address_book_dict)
            for key, value in address_book_dict.items():
                print(space)
                print("Address Book Name is: ", key)
                # calling the printing function
                printing_details_on_console(value)
            continue

        if user_input == 2:
            # Will be displaying the dic of person by city and state
            city_person_dict = dictionary_of_city_and_person(address_book_dict)
            continue

        if user_input == 3:
            city_person_dict = dictionary_of_city_and_person(address_book_dict)
            for key, value in city_person_dict.items():
                print(
                    f"Total Number of Persons residing in {key} city are: {len(value)} and details of those are: ")
                printing_details_on_console(value)
            continue

        if user_input == 4:
            state_person_dict = dictionary_of_state_and_person(address_book_dict)
            for key, value in state_person_dict.items():
                print(
                    f"Total Number of Persons residing in {key} state are: {len(value)} and details of those are: ")
                printing_details_on_console(value)
            continue

        if user_input == 5:
            sorted_name_list = sorting_entries_by_person_name(address_book_dict)
            printing_details_on_console(sorted_name_list)
            continue

        if user_input == 6:
            sorted_by_city_list = sorting_entries_by_city(address_book_dict)
            printing_details_on_console(sorted_by_city_list)
            continue
        if user_input == 7:
            sorted_by_state_list = sorting_entries_by_state(address_book_dict)
            printing_details_on_console(sorted_by_state_list)
            continue
        if user_input == 8:
            sorted_by_zip_list = sorting_entries_by_zip(address_book_dict)
            printing_details_on_console(sorted_by_zip_list)
            continue
        if user_input is not 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8:
            break

