"""Phone assistant to search for a phone number in the database"""

import argparse

PHONE_NUMBERS = [380675674432, 380672832500, 380983567721]


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