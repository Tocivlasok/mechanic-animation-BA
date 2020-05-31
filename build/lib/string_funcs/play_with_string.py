"""
Spyder Editor.

#!/usr/bin/env/
If several versions of Python installed,
/usr/bin/env will ensure the interpreter used is the first one on your environment's $PATH.
You can hardcode #!/usr/bin/python; that's ok, but less flexible.

@author: Tocivlasok

@directory: mechanic_animations/string_funcs/
"""


import argparse


def __init__(self):
    # Return exits the current function or method.
    # Pass is a null operation and allows execution to continue at the next statement.
    pass


def reverse_str(str_passed):
    """Return reversed string."""
    # check whether user input is not blank
    # print("from reverse_str()")
    if not bool(str_passed):
        # print("You have entered an empty string.")
        return False
    # check whether user input is of type str
    # not needed as argparse in main() takes all the inputs as strings
    elif not isinstance(str_passed, str):
        # print("You should have entered a string.")
        return False
    # return reverserd string
    else:
        str_to_transform = (''.join(reversed(str_passed)))
        return str_to_transform


def upper_case_str(str_passed):
    """Return upperCased string."""
    # check whether user input is not blank
    # print("from upper_case_str()")
    if not bool(str_passed):
        # print("You have entered an empty string.")
        return False
    # check whether user input is of type str
    # not needed as argparse in main() takes all the inputs as strings
    elif not isinstance(str_passed, str):
        # print("You should have entered a string.")
        return False
    # return upperCased string
    else:
        str_to_transform = str_passed.upper()
        return str_to_transform


def print_outs(string_to_be_processed):
    """Print transformations results."""
    # print("from print_outs()")
    print("Your string Reversed: ", end='')
    print(str(reverse_str(string_to_be_processed)))
    print("Your string UpperCased: ", end='')
    print(str(upper_case_str(string_to_be_processed)))
    print("Your string Transformed in peculiar way: ", end='')
    print(str(upper_case_str(str(reverse_str(string_to_be_processed)))))
    return


def main(*args):
    """Prompts the user to enter his/her string.

    Converts it in 3 different ways.
    """
    print("\nFrom the console:")
    parser = argparse.ArgumentParser()
    if(len(args) == 0):
        parser.add_argument("str_to_transform", help="Enter a string to be transformed: ", type=str)
        args = parser.parse_args()
        if(args.str_to_transform):
            print_outs(args.str_to_transform)
        else:
            print("You have entered an invalid argument.")
            return False
    else:
        print_outs(args)

    return True


if __name__ == '__main__':
    main()
