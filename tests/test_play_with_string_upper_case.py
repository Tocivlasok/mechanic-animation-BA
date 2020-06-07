"""
Created on Thu May 28 00:12:35 2020.

@author: Tocivlasok
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../")
from string_funcs import play_with_string
import pytest


def test_upper_case_str_single_word():
    """Test for upper_case_str(single word).

     # , "Failure at -single word- inarg."
     """
    assert play_with_string.upper_case_str("lollypop") == "LOLLYPOP"


def test_upper_case_str_multiple_words():
    """Test for upper_case_str(multiple words)."""
    assert play_with_string.upper_case_str("two worDs") == "TWO WORDS"


def test_upper_case_str_number_int():
    """Test for upper_case_str(number integer)."""
    with pytest.raises(ValueError) as errinfo:
        play_with_string.upper_case_str(7230)
    assert "Value is not string." in str(errinfo.value)


def test_upper_case_str_number_float():
    """Test for upper_case_str(number float)."""
    with pytest.raises(ValueError) as errinfo:
        play_with_string.upper_case_str(8.28427)
    assert "Value is not string." in str(errinfo.value)


def test_upper_case_str_none():
    """Test for upper_case_str(None)."""
    with pytest.raises(ValueError) as errinfo:
        play_with_string.upper_case_str(None)
    assert "Value is blank." in str(errinfo.value)


def test_upper_case_str_blank():
    """Test for upper_case_str("").

    # , "Passed: empty string. Minimum 1 argument required."
    """
    with pytest.raises(ValueError) as errinfo:
        play_with_string.upper_case_str("")
    assert "Value is blank." in str(errinfo.value)


def test_upper_case_str_special_chars():
    """Test for upper_case_str(special chars)."""
    assert play_with_string.upper_case_str("!?-.ň§ôäú´=""") == "!?-.Ň§ÔÄÚ´="""


def test_upper_case_str_char10():
    """Test for upper_case_str(new_line())."""
    assert play_with_string.upper_case_str("\n")


def test_upper_case_str_list_of_values():
    """Test for upper_case_str(list)."""
    with pytest.raises(ValueError) as errinfo:
        play_with_string.upper_case_str(["mio", 125, {"!", "↔"}])
    assert "Value is not string." in str(errinfo.value)


def test_upper_case_str_list_of_int_values():
    """Test for upper_case_str(list)."""
    with pytest.raises(ValueError) as errinfo:
        play_with_string.upper_case_str([1, 7, 4])
    assert "Value is not string." in str(errinfo.value)
