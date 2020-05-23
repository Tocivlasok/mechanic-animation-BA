"""Spyder Editor."""

import argparse


def reverse_str(str_name):
    """Return reversed string."""
    str_to_transform = (''.join(reversed(str_name)))
    return str_to_transform


def upper_case_str(str_name):
    """Return upperCased string."""
    str_to_transform = str_name.upper()
    return str_to_transform


def main():
    """Prompts the user to enter his/her string.

    Converts it in 3 different ways.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("str_to_transform", help="Enter a string to be transformed: ", type=str)
    args = parser.parse_args()

    print("Your string Reversed: " + reverse_str(args.str_to_transform))
    print("Your string UpperCased: " + upper_case_str(args.str_to_transform))
    print(
        "Your string Transformed in peculiar way: "
        + upper_case_str(reverse_str(args.str_to_transform))
    )


if __name__ == '__main__':
    main()
