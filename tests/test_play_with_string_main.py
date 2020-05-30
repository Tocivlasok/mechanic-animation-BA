"""
Created on Thu May 28 01:51:33 2020.

@author: Tocivlasok
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../")
from string_funcs import play_with_string


# When you run pytest --cov it looks for all the test_* scripts
# and runs all the test_* functions.

# optionally I can include a test function to call main(args)
# cmd will autommatically add cmd line args to the main
# pass list of values to the main
# result = main(["-r", "-u", "hello world"])


def __init__(self):
    pass


def test_main_single_word():
    """Test for main(single word)."""
    assert play_with_string.main(["lollypop"]) is True


def test_main_multiple_words():
    """Test for main(multiple words)."""
    assert play_with_string.main("two worDs") is True


def test_main_number_int():
    """Test for main(number integer)."""
    assert play_with_string.main(int(7230)) is True


def test_main_number_float():
    """Test for main(number float)."""
    assert play_with_string.main(8.28427) is True


def test_main_blank():
    """Test for main("")."""
    assert play_with_string.main("") is True  # , "Passed: empty string. Minimum 1 argument required."


def test_main_special_chars():
    """Test for main(special chars)."""
    assert play_with_string.main("!?-.ň§ôäú´=""") is True


def test_main_char10():
    """Test for main(new_line())."""
    assert play_with_string.main("\n") is not False


def test_main_list_of_values_of_multiple_types():
    """Test for main(list)."""
    assert play_with_string.main([258, 0.605551, "Hello Yourself!"]) is True


def test_main_list_of_str_values():
    """Test for main(list)."""
    assert play_with_string.main(["-u", "O-o", "H!"]) is True


if __name__ == "__main__":
    print("Passed.")
