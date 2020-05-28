"""
Created on Sat May 23 11:18:32 2020.

@author: Tocivlasok
"""

from play_with_string import reverse_str
# import sys
# sys.path.append('C:/Users/user/Desktop/Sima/_gitRepo_MechanicBA/play_with_string.py')

# When you run pytest --cov it looks for all the test_* scripts
# and runs all the test_* functions.

# MyTestsSoFar ~ they simply assert, the function returns a result (is not None),
# so they will always be true.
# add: assert upper_case_str("lollypop") == "LOLLYPOP".
# pytest will give me the error message and line number when the assertion fails.

# if you specify a message with the assertion, then no assertion introspection takes places
# and the message will be simply shown in the traceback. # assert expr, "mssg"


def __init__(self):
    pass


def test_reverse_str_single_word():
    """Test for reverse_str(single word)."""
    assert reverse_str("lollypop") == "popyllol"  # , "Failure at -single word- inarg."


def test_reverse_str_multiple_words():
    """Test for reverse_str(multiple words)."""
    assert reverse_str("two worDs") == "sDrow owt"


def test_reverse_str_number_int():
    """Test for reverse_str(number integer)."""
    assert reverse_str(7230) is False


def test_reverse_str_number_float():
    """Test for reverse_str(number float)."""
    assert reverse_str(8.28427) is False


def test_reverse_str_blank():
    """Test for reverse_str("")."""
    assert reverse_str("") is False  # , "Passed: empty string. Minimum 1 argument required."


def test_reverse_str_special_chars():
    """Test for reverse_str(special chars)."""
    assert reverse_str("!?-.ň§ôäú´=""") == "=´úäô§ň.-?!"


def test_reverse_str_char10():
    """Test for reverse_str(new_line())."""
    assert reverse_str("\n") is not False


def test_reverse_str_list_of_values():
    """Test for reverse_str(list)."""
    assert reverse_str(["mio", 125, {"!", "↔"}]) is False


if __name__ == "__main__":
    print("Passed.")
