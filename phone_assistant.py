"""Phone assistant to search for a phone number in the database"""

import argparse
import re

PHONE_NUMBERS = [380675674432, 380672832500, 380983567721]


def phone_number_search(argv='38067'):
    """Search for valid phone numbers"""

    correct_phone_numbers = []
    phone_number_regex = re.escape(argv) + r'[0-9]{' + str(12-len(argv)) + r'}$'
    phone_number_pattern = re.compile(phone_number_regex)

    for item in PHONE_NUMBERS:
        if phone_number_pattern.match(str(item)):
            correct_phone_numbers.append(item)

    return correct_phone_numbers


def arg_parse():
    """Initialize argument parser"""

    arg_parser = argparse.ArgumentParser(description='Process integer input')
    arg_parser.add_argument('integer',
                            type=int,
                            help='An integer input to search for a phone number')

    return arg_parser


def main():
    """Main entry point"""


if __name__ == '__main__':
    main()
