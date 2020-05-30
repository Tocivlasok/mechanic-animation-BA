"""
Created on Thu May 28 00:12:35 2020.

@author: Tocivlasok
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../")
from string_funcs import play_with_string


def __init__(self):
    pass


def test_upper_case_str_single_word():
    """Test for upper_case_str(single word)."""
    assert play_with_string.upper_case_str("lollypop") == "LOLLYPOP"  # , "Failure at -single word- inarg."


def test_upper_case_str_multiple_words():
    """Test for upper_case_str(multiple words)."""
    assert play_with_string.upper_case_str("two worDs") == "TWO WORDS"


def test_upper_case_str_number_int():
    """Test for upper_case_str(number integer)."""
    assert play_with_string.upper_case_str(7230) is False


def test_upper_case_str_number_float():
    """Test for upper_case_str(number float)."""
    assert play_with_string.upper_case_str(8.28427) is False


def test_upper_case_str_none():
    """Test for upper_case_str(None)."""
    assert play_with_string.upper_case_str(None) is False


def test_upper_case_str_blank():
    """Test for upper_case_str("")."""
    assert play_with_string.upper_case_str("") is False  # , "Passed: empty string. Minimum 1 argument required."


def test_upper_case_str_special_chars():
    """Test for upper_case_str(special chars)."""
    assert play_with_string.upper_case_str("!?-.ň§ôäú´=""") == "!?-.Ň§ÔÄÚ´="""


def test_upper_case_str_char10():
    """Test for upper_case_str(new_line())."""
    assert play_with_string.upper_case_str("\n") is not False


def test_upper_case_str_list_of_values():
    """Test for upper_case_str(list)."""
    assert play_with_string.upper_case_str(["mio", 125, {"!", "↔"}]) is False


def test_upper_case_str_list_of_int_values():
    """Test for upper_case_str(list)."""
    assert play_with_string.upper_case_str([1, 7, 4]) is False


if __name__ == "__main__":
    print("Passed.")
