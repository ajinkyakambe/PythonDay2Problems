# Start of Address Book Program

'''
Ability to create a Contacts in Address
Book with first and last names, address,
city, state, zip, phone number and
email...
'''


class Contacts():

    def __init__(self, first_name, last_name, address, city, state, zip, phone_number, email):
        """
            Description: Constructor of Contacts Class
            Parametres: Takes class fields
            Retuns: None, Just initialize the values of object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone_number = phone_number
        self.email = email

    # https://www.educative.io/answers/what-is-the-str-method-in-python
    def __str__(self):
        """
            Description: To return textual content of the Contacts class Object
            Parameters: Takes Instance (Object) of class as arguments
            Returns: Returns String Representation of object
        """
        return f"Full Name is {self.first_name} {self.last_name}\nFull address is {self.address},{self.city},{self.state},{self.zip}\nPhone Number & email is {self.phone_number} and {self.email} respectively"


def add_contact():
    """
            Description: Adding Contact Details form Console
            Parameters: None
            Returns: Returns contact class object
    """
    print("Adding the contact")
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    address = input("Enter the address: ")
    city = input("Enter city name: ")
    state = input("Enter state name: ")
    zip = input("Enter zip code: ")
    phone_number = input("Enter phone_number: ")
    email = input("Enter email address: ")
    contact_obj = Contacts(first_name, last_name, address,
                           city, state, zip, phone_number, email)
    return contact_obj


def Storing_contacts_in_data():
    """
           Description: Adding Contact Details form Console in list
           Parameters: None
           Returns: Returns a list containing objects of Contact Class.
    """
    while (True):
        contact_obj = add_contact()
        contacts_data.append(contact_obj)
        contacts_to_add_choice = input(
            "Enter \"Y\" for adding more & \"N\" to stop adding: ")
        if contacts_to_add_choice.upper() == "N":
            # upper is for uppercase
            break
    return contacts_data

def Editing_contacts(contact_data_list):
    """
        Description: Editing Contact Details form Console
        Parameters: None
        Returns: Returns a list containing objects
    """
    edited_person_name = input("Enter the name of person, whom details you want to edit: ").upper()
    try:
        for item in contact_data_list:
            if item.first_name.upper() == edited_person_name:
                choice = input(
                    "Enter choice u want to edit:\n 1 : FN,2 : LN,3 : Address,4 : City,5 : State,6 : ZIP,7 : Phone,8 : Email")
                if (choice == "1"):
                    fn = input("Enter updated first name: ")
                    item.first_name = fn
                elif (choice == "2"):
                    ln = input("Enter updated last name: ")
                    item.last_name = ln
                elif (choice == "3"):
                    addrs = input("Enter updated address: ")
                    item.address = addrs
                elif (choice == "4"):
                    city = input("Enter updated city: ")
                    item.city = city
                elif (choice == "5"):
                    state = input("Enter updated state: ")
                    item.state = state
                elif (choice == "6"):
                    zip = input("Enter updated zip: ")
                    item.zip = zip
                elif (choice == "7"):
                    phn_no = input("Enter updated phn number: ")
                    item.phone_number = phn_no
                elif (choice == "8"):
                    email = input("Enter updated email: ")
                    item.email = email
                else:
                    print("Invalid Choice")
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    contacts_data = []
    Storing_contacts_in_data()
    user_choice = input("Do u want to edit Contacts \"Y\" OR \"N\":").upper()
    if (user_choice.upper() == "Y"):
        Editing_contacts(contacts_data)
    for item in contacts_data:
        print() # Blank line
        print(str(item))
        print() # Blank line
