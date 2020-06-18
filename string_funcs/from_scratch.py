"""
Created on Wed Jun 17 21:35:44 2020.

@author: Tocivlasok
"""

import sys
import argparse
import pandas as pd
import re


def create_parser_N(user_input):
    """Create ArgumentParser object 'parser'.

    Parser processes each sign provided by user as a string.
    User can input multiple arguments for each parser argument option.
    Any argument provided by user before any valid parser argument
    is considered a dummy word.
    Return 'parser' and arguments Namespace object 'args'.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'dummy_words',
        # metavar='N',
        type=str,
        nargs='*',
        help='IGNORED. Dummy words passed with no relation to any of valid arguments.')

    """
    parser.add_argument(
        '--concat',
        dest='together_str',
        action='store_const',
        const='function_one',
        default='default_none',
        help='strings for concatenation')
    """
    parser.add_argument(
        '-r',
        nargs='*',
        type=str,
        help='REVERSE. String to be reversed. \
        Result printed to console.',
        )
    parser.add_argument(
        '-u',
        nargs='*',
        type=str,
        help='UPPERCASE. String to be upper-cased. \
        Result printed to console.',
        )
    parser.add_argument(
        '-c',
        nargs='*',
        type=str,
        help='COMBINE (REVERSED and UPPERCASED). \
        string to be reversed and subsequently upper-cased. \
        Result printed to console.')

    parser.add_argument(
        '-frs',
        nargs='*',
        type=str,
        help="FILE REVERSE STRINGS. Enter full path to the *.txt file. \
        Text will be reversed string by string. \
        Result will be stored in the same folder as original file \
        with name: re.sub('.txt', '', filename) \
        and with suffix: '_strings_reversed.txt'. ")
    parser.add_argument(
        '-fus',
        nargs='*',
        type=str,
        help="FILE UPPERCASE STRINGS. Enter full path to the *.txt file. \
        Text will be upper-cased string by string. \
        Result will be stored in the same folder as original file \
        with name: re.sub('.txt', '', filename) \
        and with suffix: '_strings_uppercased.txt'. ")
    parser.add_argument(
        '-fcs',
        nargs='*',
        type=str,
        help="FILE COMBINE (REVERSE and UPPERCASE STRINGS). \
        Enter full path to the *.txt file. \
        Text will be reversed and subsequently upper-cased string by string. \
        Result will be stored in the same folder as original file \
        with name: re.sub('.txt', '', filename) \
        and with suffix: '_strings_combined.txt'. ")

    parser.add_argument(
        '-frl',
        nargs='*',
        type=str,
        help="FILE REVERSE LINES. Enter full path to the *.txt file. \
        Text will be reversed line by line. \
        Result will be stored in the same folder as original file \
        with name: re.sub('.txt', '', filename) \
        and with suffix: '_lines_reversed.txt'. ")
    # -ful would be the same as -fus
    parser.add_argument(
        '-fcl',
        nargs='*',
        type=str,
        help="FILE COMBINE (REVERSE and UPPERCASE LINES). \
        Enter full path to the *.txt file. \
        Text will be reversed and subsequently upper-cased line by line. \
        Result will be stored in the same folder as original file \
        with name: re.sub('.txt', '', filename) \
        and with suffix: '_lines_combined.txt'. ")

    parser.add_argument(
        '-frw',
        nargs='*',
        type=str,
        help="FILE REVERSE WHOLE. Enter full path to the *.txt file. \
        Text will be reversed from bottom up line by line. \
        Result will be stored in the same folder as original file \
        with name: re.sub('.txt', '', filename) \
        and with suffix: '_whole_reversed.txt'. ")
    # -fuw would be the same as -fus
    parser.add_argument(
        '-fcw',
        nargs='*',
        type=str,
        help="FILE COMBINE (REVERSE and UPPERCASE WHOLE). \
        Enter full path to the *.txt file. \
        Text will be reversed and subsequently upper-cased from bottom up line by line. \
        Result will be stored in the same folder as original file \
        with name: re.sub('.txt', '', filename) \
        and with suffix: '_whole_combined.txt'. ")

    args = parser.parse_args(user_input)
    return parser, args


def standardize_filepath(filepath):
    """Change slashes to double-back-slashes.

    Concatenate and return as regex.
    """
    speciality = "▀■░▒▓■▄"
    path_standardized = (((filepath.replace('\\\\', speciality)).replace('\\', '\\\\')).replace("/", '\\\\')).replace(speciality, '\\\\')
    # path_standardized = (filepath.replace('\\', '\\\\')).replace("/", '\\\\')
    return 'r"' + path_standardized + '"'


def file_read_content(filepath):
    """Read content of *.txt file.
    Return whole text string object.
    Return pandas DataFrame object for looping through lines/words.
    """
    with open(filepath, 'r') as filehandle:
        whole_text = filehandle.read()
    df = pd.DataFrame()
    df = pd.read_csv(filepath,
                     sep='\n',
                     header=None)
    return whole_text, df


def compose_filepath_for_result(filepath, suffix):
    truncated_end = re.sub('.txt', '', filepath)
    func_suff = {'frs': '_strings_reversed.txt',
                 'fus': '_strings_uppercased.txt',
                 'fcs': '_strings_combined.txt',
                 
                 'frl': '_lines_reversed.txt',
                 'fcl': '_lines_combined.txt',
                 
                 'frw': '_whole_reversed.txt',
                 'fuw': '_whole_combined.txt'}
    return  standardize_filepath(truncated_end + func_suff.get(suffix))
    

def file_write_content(filepath_with_suffix, data):
    """Write data to *.txt file generated from compose_filepath_for_result()"""
    # TODO: update this function to process strings and also tuples
    with open(filepath_with_suffix, 'w') as filehandle:
         filehandle.write(data)
    pass


def run_functiton_on_data(func, data):
    """Pass function as paramater. Apply function to data."""
    func_dict = {'reverse_str': reverse_str,
                 'upper_case_str': upper_case_str,
                 'transform_string': transform_string}
    return func_dict.get(func)(data)


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
    """Return string reversed and simultaneously upppercased."""
    return upper_case_str(reverse_str(str_passed))


def main(*args):
    """Process input arguments passed by the user from command line."""
    parser, args = create_parser_N(sys.argv[1:])

    # -r    REVERSE
    args.r
    print(run_functiton_on_data('reverse_str', args.r[0]))

    # -u    UPPERCASE
    args.u

    # -c    COMBINED (REVERSE AND UPPERCASE)
    args.c

    # -frs  FILE REVERSE STRINGS
    args.frs
    file_write_content(args.frs[0], ("vfr"))
    # update file_write_content() to accept touples and also strings

    # -fus  FILE UPPERCASE STRINGS
    args.fus

    # -fcs  FILE COMBINE STRINGS (REVERSE AND UPPERCASE)
    args.fcs

    # -frl  FILE REVERSE LINES
    args.frl

    # -fcl  FILE COMBINE LINES (REVERSE AND UPPERCASE)
    args.fcl

    # -frw  FILE REVERSE WHOLE
    args.frw
    print(compose_filepath_for_result(r"C:\Users\user\Desktop\Folder\nta.txt", 'frw'))

    # -fcw  FILE COMBINE WHOLE (REVERSE AND UPPERCASE)
    args.fcw


# =============================================================================
#     # -r
#     if(args.r):
#         print('Reversed:')
#         for data_item in args.r:
#             print(reverse_str(data_item))
#         print()
#     else:
#         pass
#     # -u
#     if(args.u):
#         print('Upper-cased:')
#         for data_item in args.u:
#             print(upper_case_str(data_item))
#         print()
#     else:
#         pass
#
#     frs_files = args.frs
#     for item in frs_files:
#         whole_text, df = file_read_content(item)
#         print(whole_text)
#         print()
# =============================================================================

    return True

if __name__ == '__main__':
    main()
