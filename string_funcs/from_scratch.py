"""
Created on Wed Jun 17 21:35:44 2020.

@author: Tocivlasok
"""

import sys
import argparse
import pandas as pd
import re
import os


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

# not used
# =============================================================================
# def standardize_filepath(filepath):
#     """Change slashes to double-back-slashes.
#
#     Concatenate and return as regex.
#     """
#     speciality = "▀■░▒▓■▄"
#     path_standardized = (((filepath.replace('\\\\', speciality)).replace('\\', '\\\\')).replace("/", '\\\\')).replace(speciality, '\\\\')
#     # path_standardized = (filepath.replace('\\', '\\\\')).replace("/", '\\\\')
#     return 'r"' + path_standardized + '"'
# =============================================================================


def file_read_content(filepath):
    """Read content of *.txt file.

    Return whole text string object.
    Return pandas DataFrame object for looping through lines/words.
    """
    # TODO raise error/exception if file not found
    # TODO limit file size
    # TODO raise error/exception when empty file passed
    with open(filepath, 'r') as filehandle:
        whole_text = filehandle.read()
        # lines = whole_text.splitlines()
        # words = lines.split(' ')
    # lines = tuple(open(filepath, 'r'))
    # df = pd.DataFrame()
    # df = pd.read_csv(filepath, sep='\n', header=None)
    # return whole_text, df
    return whole_text

# =============================================================================
#     try:
#         with open(filepath, 'r') as filehandle:
#             whole_text = filehandle.read()
#             # lines = whole_text.splitlines()
#             # words = lines.split(' ')
#         # lines = tuple(open(filepath, 'r'))
#         # df = pd.DataFrame()
#         # df = pd.read_csv(filepath, sep='\n', header=None)
#         # return whole_text, df
#         return whole_text
#     except (FileNotFoundError, IOError):
#         print("Wrong file or file path")
#         # if not os.path.isfile("nothing.txt"):
#             # raise FileNotFoundError
#     pass
# =============================================================================


def compose_filepath_for_result(filepath, argument):
    """Create filepath with corresponding suffix.

    Results to be written into.
    Realtes only to '-f*' argument options - process data from a text file.
    """
    truncated_end = re.sub('.txt', '', filepath)
    func_argm = {'frs': '_strings_reversed.txt',
                 'fus': '_strings_uppercased.txt',
                 'fcs': '_strings_combined.txt',

                 'frl': '_lines_reversed.txt',
                 'fcl': '_lines_combined.txt',

                 'frw': '_whole_reversed.txt',
                 'fuw': '_whole_combined.txt'
                 }
    # return standardize_filepath(truncated_end + func_argm.get(argument))
    return truncated_end + func_argm.get(argument)


def file_write_content(filepath_with_suffix, data):
    """Write string data to *.txt file generated from compose_filepath_for_result()."""
    with open(filepath_with_suffix, 'w') as filehandle:
        if isinstance(data, str):
            filehandle.write(data)
        elif isinstance(data, tuple):
            filehandle.write(' '.join(str(x) for x in data))
        elif isinstance(data, list):
            filehandle.write('\n'.join(data))
    pass
    # new line chr(10) "\n" "\r\n" is messy


# =============================================================================
# def file_write_content_tuple(filepath_with_suffix, data):
#     """Write tuple data to *.txt file generated from compose_filepath_for_result()"""
#     with open(filepath_with_suffix, 'w') as filehandle:
#         filehandle.write(' '.join(str(x) for x in data))
#     pass
# =============================================================================


def run_functiton_on_data(func, data):
    """Pass function as paramater. Apply function to data."""
    func_dict = {'r': reverse_str,
                 'u': upper_case_str,
                 'c': transform_string
                 }
    return func_dict.get(func)(data)


def run_func_on_data_with_mssg(argument, data):
    """Process data [str/tuple] only when the object is not empty.

    Printing basic fuctions output to the console.
    """
    argument_mssg = {'r':   "\nRversed",
                     'u':   "\nUppergased",
                     'c':   "\nReversed & Uppercased"
                     }
    func_dict = {'r':   reverse_str,
                 'u':   upper_case_str,
                 'c':   transform_string
                 }
    # TODO could be 1 ditionary
    # print(argument_mssg.get(argument)[1])
    if not data:
        pass
    else:
        print(argument_mssg.get(argument))
        for item in data:
            print(func_dict.get(argument)(item))
            # print(run_functiton_on_data(argument, item))
    pass


def run_func_on_data_with_mssg_file_args(argument, data):
    """Process data = filenames [str/tuple] only when the object is not empty."""
    argument_mssg = {'frs': '\nFile - reversed - string by string.',
                     'fus': '\nFile - uppercase - string by string.',
                     'fcs': '\nFile - reverse and uppercase - string by string.',

                     'frl': '\nFile - reverse line by line.',
                     'fcl': '\nFile - reverse and uppercase line by line.',

                     'frw': '\nFile - reverse - whole.',
                     'fuw': '\nFile - reverse and uppercase - whole.'
                     }
    if not data:
        pass
    else:
        for file in data:
            destpath = file_processing(argument, file)
            print(argument_mssg.get(argument) + '\nSee results in: ' + destpath)
    pass


def reverse_str(str_passed):
    """Return reversed string."""
    if isinstance(str_passed, str):
        return (''.join(reversed(str_passed)))
    elif isinstance(str_passed, tuple) or isinstance(str_passed, list):
        results = []
        for item in str_passed:
            # TODO try to convert to string if item not string
            results.append((''.join(reversed(item))))
        return results
    else:
        # TODO try to convert to string
        pass
# =============================================================================
#     # check whether user input is not blank
#     if not bool(str_passed):
#         # print("reverse: You have entered an empty string.")
#         raise ValueError("Value is blank.")
#     # check whether user input is of type str
#     elif not isinstance(str_passed, str):
#         # print("reverse: You should have entered a string.")
#         raise ValueError("Value is not string.")
#     else:
#         str_to_transform = (''.join(reversed(str_passed)))
#         return str_to_transform
# =============================================================================


def upper_case_str(str_passed):
    """Return upperCased string."""
    if isinstance(str_passed, str):
        return str_passed.upper()
    elif isinstance(str_passed, tuple) or isinstance(str_passed, list):
        results = []
        for item in str_passed:
            # TODO try to convert to string if item not string
            results.append(item.upper())
        return results
    else:
        # TODO try to convert to string
        pass
# =============================================================================
#     # check whether user input is not blank
#     if not bool(str_passed):
#         raise ValueError("Value is blank.")
#     # check whether user input is of type str
#     elif not isinstance(str_passed, str):
#         raise ValueError("Value is not string.")
#     else:
#         str_to_transform = str_passed.upper()
#         return str_to_transform
# =============================================================================


def transform_string(str_passed):
    """Return string reversed and subsequently upppercased."""
    return upper_case_str(reverse_str(str_passed))


def file_processing(argument, file):
    """."""
    # function to perform - r/u/c
    func = argument[1]
    # granularity - s/l/w
    gran = argument[2]

    destpath = compose_filepath_for_result(file, argument)
    data = file_read_content(file)

    # txtfile output stripping based on granularity
    gran_switcher = {
        'w': data,
        'l': data.splitlines(),
        's': data.splitlines()
        # (data.splitlines()).split(' ')
        # lines = data.splitlines()
        # words = lines.split(' ')
        # data = words
        }

    results = []
    data_granular = gran_switcher.get(gran, -1)
    if gran == 'w':
        pass  # process whole data as 1 string
        results = run_functiton_on_data(func, data_granular)
    elif gran == 'l':
        for item in data_granular:
            reversed_line = run_functiton_on_data(func, item)
            # print(reversed_line)
            results.append(reversed_line)
            # results = results + (reversed_line,)
    elif gran == 's':
        for line in data_granular:
            # print('\nline: ' + line)
            words = re.split(' ', line)
            # print('type(words): ' + str(type(words)))
            # print('words: ', end=" ")
            # print(words)
            processed_strings_in_line = run_functiton_on_data(func, words)
            # print('reversed_strings_in_line: ', end=" ")
            # print(reversed_strings_in_line)
            processed_strings_in_line_as_1_string = ' '.join(processed_strings_in_line)
            # print(reversed_strings_in_line_as_1_string)
            results.append(processed_strings_in_line_as_1_string)
    else:
        # there simply can't be such a case
        pass

    file_write_content(
        destpath,
        results
    )

    return destpath


def main(*args):
    """Process input arguments passed by the user from command line."""
    parser, args = create_parser_N(sys.argv[1:])

    # -r    args.r   REVERSE
    run_func_on_data_with_mssg('r', args.r)

    # -u    UPPERCASE
    run_func_on_data_with_mssg('u', args.u)

    # -c    COMBINED (REVERSE AND UPPERCASE)
    run_func_on_data_with_mssg('c', args.c)

    # -frs  FILE REVERSE STRINGS
    run_func_on_data_with_mssg_file_args('frs', args.frs)

    # -fus  FILE UPPERCASE STRINGS
    run_func_on_data_with_mssg_file_args('fus', args.fus)

    # -fcs  FILE COMBINE STRINGS (REVERSE AND UPPERCASE)
    run_func_on_data_with_mssg_file_args('fcs', args.fcs)

    # -frl  FILE REVERSE LINES
    run_func_on_data_with_mssg_file_args('frl', args.frl)

    # -fcl  FILE COMBINE LINES (REVERSE AND UPPERCASE)
    run_func_on_data_with_mssg_file_args('fcl', args.fcl)

    # -frw  FILE REVERSE WHOLE
    run_func_on_data_with_mssg_file_args('frw', args.frw)

    # -fcw  FILE COMBINE WHOLE (REVERSE AND UPPERCASE)
    run_func_on_data_with_mssg_file_args('fcw', args.fcw)

    return True


if __name__ == '__main__':
    main()
