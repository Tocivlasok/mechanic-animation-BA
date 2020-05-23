"""Spyder Editor."""

import argparse


def reverse_str(str_passed):
    """Return reversed string."""
    # check whether user input is not blank
    if not bool(str_passed):
        print("You have entered an empty string.")

    # check whether user input is of type str
    # not needed as argparse in main() takes all the inputs as strings
    elif not isinstance(str_passed, str):
        print("You should have entered a string.")

    # return reverserd string
    else:
        str_to_transform = (''.join(reversed(str_passed)))
        return str_to_transform

    return


def test_reverse_str_single_word():
    """Test for reverse_str(single word)."""
    assert reverse_str("lollypop"), "test failed"


def test_reverse_str_multiple_words():
    """Test for reverse_str(multiple words)."""
    assert reverse_str("More than just one word"), "test failed"


def test_reverse_str_special_chars():
    """Test for reverse_str(special chars)."""
    assert reverse_str("!?-.ň§ôäú´="""), "test failed"


def upper_case_str(str_passed):
    """Return upperCased string."""
    # check whether user input is not blank
    if not bool(str_passed):
        print("You have entered an empty string.")

    # check whether user input is of type str
    # not needed as argparse in main() takes all the inputs as strings
    elif not isinstance(str_passed, str):
        print("You should have entered a string.")

    # return upperCased string
    else:
        str_to_transform = str_passed.upper()
        return str_to_transform

    return


def test_upper_case_str_single_word():
    """Test for upper_case_str(single word)."""
    assert upper_case_str("lollypop"), "test failed"


def test_upper_case_str_multiple_words():
    """Test for upper_case_str(multiple words)."""
    assert upper_case_str("More than just one word"), "test failed"


def test_upper_case_str_special_chars():
    """Test for upper_case_str(special chars)."""
    assert upper_case_str("!?-.ň§ôäú´="""), "test failed"


def main():
    """
    Prompts the user to enter his/her string.

    Converts it in 3 different ways.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("str_to_transform", help="Enter a string to be transformed: ", type=str)
    args = parser.parse_args()

    print("Your string Reversed: " + str(reverse_str(args.str_to_transform)))
    print("Your string UpperCased: " + str(upper_case_str(args.str_to_transform)))
    print(
        "Your string Transformed in peculiar way: "
        + str(upper_case_str(str(reverse_str(args.str_to_transform))))
    )


if __name__ == '__main__':
    main()
