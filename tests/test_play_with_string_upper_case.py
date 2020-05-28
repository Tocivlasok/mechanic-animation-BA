"""
Created on Thu May 28 00:12:35 2020.

@author: Tocivlasok
"""

from play_with_string import upper_case_str
# import sys
# sys.path.append('C:/Users/user/Desktop/Sima/_gitRepo_MechanicBA/play_with_string.py')


def __init__(self):
    pass


def test_upper_case_str_single_word():
    """Test for upper_case_str(single word)."""
    assert upper_case_str("lollypop") == "LOLLYPOP"  # , "Failure at -single word- inarg."


def test_upper_case_str_multiple_words():
    """Test for upper_case_str(multiple words)."""
    assert upper_case_str("two worDs") == "TWO WORDS"


def test_upper_case_str_number_int():
    """Test for upper_case_str(number integer)."""
    assert upper_case_str(7230) is False


def test_upper_case_str_number_float():
    """Test for upper_case_str(number float)."""
    assert upper_case_str(8.28427) is False


def test_upper_case_str_blank():
    """Test for upper_case_str("")."""
    assert upper_case_str("") is False  # , "Passed: empty string. Minimum 1 argument required."


def test_upper_case_str_special_chars():
    """Test for upper_case_str(special chars)."""
    assert upper_case_str("!?-.ň§ôäú´=""") == "!?-.Ň§ÔÄÚ´="""


def test_upper_case_str_char10():
    """Test for upper_case_str(new_line())."""
    assert upper_case_str("\n") is not False


def test_upper_case_str_list_of_values():
    """Test for upper_case_str(list)."""
    assert upper_case_str(["mio", 125, {"!", "↔"}]) is False


if __name__ == "__main__":
    print("Passed.")
