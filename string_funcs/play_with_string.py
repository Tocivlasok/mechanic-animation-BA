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
import sys

def reverse_str(str_passed):
    """Return reversed string."""
    # check whether user input is not blank
    if not bool(str_passed):
        # print("reverse: You have entered an empty string.")
        raise ValueError("Value is blank.")
    # check whether user input is of type str
    elif not isinstance(str_passed, str):
        # print("reverse: You should have entered a string.")
        raise ValueError("Value is not string.")
    else:
        str_to_transform = (''.join(reversed(str_passed)))
        return str_to_transform


def upper_case_str(str_passed):
    """Return upperCased string."""
    # check whether user input is not blank
    if not bool(str_passed):
        raise ValueError("Value is blank.")
    # check whether user input is of type str
    elif not isinstance(str_passed, str):
        raise ValueError("Value is not string.")
    else:
        str_to_transform = str_passed.upper()
        return str_to_transform


def transform_string(str_passed):
    """Return string transformed in 3 different ways as a touple."""
    return reverse_str(str_passed), \
        upper_case_str(str_passed), \
        upper_case_str(reverse_str(str_passed))


def main(*args):
    """Prompts the user to enter his/her string.

    Converts it in 3 different ways.
    """
    prints = ["Reversed: ", "UpperC: ", "Combined: "]
    parser = argparse.ArgumentParser()
    if(len(args) == 0):
        parser.add_argument("str_to_transform", help="Enter a string to be transformed: ", type=str)
        args = parser.parse_args()
        try:
            for function in range(len(prints)):
                print(prints[function] + "\t" + str(transform_string(args.str_to_transform)[function]))
            print("\n")
            return True
        except ValueError:
            raise Exception("You have entered an invalid argument.")

    else:
        for item in args:
            try:
                results = transform_string(item)
                for function in range(len(prints)):
                    print("main:" + prints[function] + "\t" + str(results[function]))
                print("\n")
            except ValueError:
                raise Exception("You have entered an invalid argument.")
                return False

        return True


if __name__ == '__main__':
    main()
