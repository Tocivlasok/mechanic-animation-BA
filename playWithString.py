"""Spyder Editor."""

import argparse


def reverseStr(strName):
    """Return reversed string."""
    strToTransform = (''.join(reversed(strName)))
    return strToTransform


def upperCaseStr(strName):
    """Return upperCased string."""
    strToTransform = strName.upper()
    return strToTransform


def Main():
    """Prompts the user to enter his/her string.

    Converts it in 3 different ways.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("strToTransform", help="Enter a string to be transformed: ", type=str)
    args = parser.parse_args()

    print("Your string Reversed: " + reverseStr(args.strToTransform))
    print("Your string UpperCased: " + upperCaseStr(args.strToTransform))
    print("Your string Transofrmed in peculiar way: " + upperCaseStr(reverseStr(args.strToTransform)))


if __name__ == '__main__':
    Main()
