class AddressBookException(Exception):

    def __init__(self, message):
        # To access base exception class
        super().__init__(message)