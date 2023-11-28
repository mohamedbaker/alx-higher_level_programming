''' module for func that prints full name. '''


def say_my_name(first_name, last_name=""):
    '''
    function that prints full name .
    args:
         first_name: first name.
         last_name: last name with defult value of empty str.
    raises:
           TypeError: first_name must be a string or
                         last_name must be a string.
    '''

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
