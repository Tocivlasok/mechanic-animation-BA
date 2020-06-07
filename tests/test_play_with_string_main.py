"""
Created on Thu May 28 01:51:33 2020.

@author: Tocivlasok
"""

import pytest
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


# 1
def test_main_single_word():
    """Test for main(single word)."""
    assert play_with_string.main("lollypopy")


# 2
def test_main_multiple_words():
    """Test for main(multiple words)."""
    assert play_with_string.main("two worDs")


# 3
def test_main_number_int():
    """Test for main(number integer)."""
    # assert play_with_string.main(int(7230))
    with pytest.raises(Exception) as ex:
        play_with_string.main(7230)
    assert "You have entered an invalid argument." in str(ex.value)


# 4
def test_main_number_float():
    """Test for main(number float)."""
    # assert play_with_string.main(8.28427) is None
    with pytest.raises(Exception) as ex:
        play_with_string.main(8.28427)
    assert "You have entered an invalid argument." in str(ex.value)


# 5
def test_main_none():
    """Test for main(None)."""
    # assert str(ex.value) is "You have entered an invalid argument."
    # assert play_with_string.main(None)
    with pytest.raises(Exception) as ex:
        play_with_string.main(None)
    assert "You have entered an invalid argument." in str(ex.value)


# 6
def test_main_blank():
    """Test for main("").

    Passed: empty string. Minimum 1 argument required."""
    # assert play_with_string.main("") is None
    with pytest.raises(Exception) as ex:
        play_with_string.main("")
    assert "You have entered an invalid argument." in str(ex.value)


# 7
def test_main_special_chars():
    """Test for main(special chars)."""
    assert play_with_string.main("!?-.ň§ôäú´=""")


# 8
def test_main_char10():
    """Test for main(new_line())."""
    assert play_with_string.main("\n")


# 9
def test_main_list_of_values_of_multiple_types():
    """Test for main(list of mixed types)."""
    # assert play_with_string.main([258, 0.605551, "Hello Yourself!"])
    with pytest.raises(Exception) as ex:
        play_with_string.main([258, 0.605551, "Hello Yourself!"])
    assert "You have entered an invalid argument." in str(ex.value)


# 10
def test_main_list_of_str_values():
    """Test for main(list of strings)."""
    assert play_with_string.main("-u", "O-o", "H!")


# 11
def test_main_list_of_int_values():
    """Test for main(list of numbers)."""
    # assert play_with_string.main([1, 7, 4])
    with pytest.raises(Exception) as ex:
        play_with_string.main([1, 7, 4])
    assert "You have entered an invalid argument." in str(ex.value)
