"""
Created on Sat May 23 11:18:32 2020.

@author: Tocivlasok
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../")
from string_funcs import play_with_string
import pytest


def test_transform_string_single_word():
    """Test for transform_string(single word).

     #, "Failure at -single word- inarg."
    """
    assert play_with_string.transform_string("lollypop")


def test_transform_string_multiple_words():
    """Test for transform_string(multiple words)."""
    assert play_with_string.transform_string("two worDs")


def test_transform_string_number_int():
    """Test for transform_string(number integer)."""
    # assert play_with_string.transform_string(7230) == (False, False, False)
    with pytest.raises(ValueError) as errinfo:
        play_with_string.transform_string(7230)
    assert "Value is not string." in str(errinfo.value)


def test_transform_string_number_float():
    """Test for transform_string(number float)."""
    # assert play_with_string.transform_string(8.28427) == (False, False, False)
    with pytest.raises(ValueError) as errinfo:
        play_with_string.transform_string(8.28427)
    assert "Value is not string." in str(errinfo.value)


def test_transform_string_none():
    """Test for transform_string(None)."""
    # assert play_with_string.transform_string(None) == (False, False, False)
    with pytest.raises(ValueError) as errinfo:
        play_with_string.transform_string(None)
    assert "Value is blank." in str(errinfo.value)


def test_transform_string_blank():
    """Test for transform_string("").

     #, Passed: empty string. Minimum 1 argument required."
    """
    # assert play_with_string.transform_string("") == (False, False, False)
    with pytest.raises(ValueError) as errinfo:
        play_with_string.transform_string("")
    assert "Value is blank." in str(errinfo.value)


def test_transform_string_special_chars():
    """Test for transform_string(special chars)."""
    assert play_with_string.transform_string("!?-.ň§ôäú´=""")


def test_transform_string_char10():
    """Test for transform_string(new_line())."""
    assert play_with_string.transform_string("\n")


def test_transform_string_list_of_values():
    """Test for transform_string(list)."""
    # assert play_with_string.transform_string(["mio", 125, {"!", "↔"}]) == (False, False, False)
    with pytest.raises(ValueError) as errinfo:
        play_with_string.transform_string(["mio", 125, {"!", "↔"}])
    assert "Value is not string." in str(errinfo.value)


def test_transform_string_list_of_int_values():
    """Test for transform_string(list)."""
    # assert play_with_string.transform_string([1, 7, 4]) == (False, False, False)
    with pytest.raises(ValueError) as errinfo:
        play_with_string.transform_string([1, 7, 4])
    assert "Value is not string." in str(errinfo.value)
    