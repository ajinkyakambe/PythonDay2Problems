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