"""Phone assistant to search for a phone number in the database"""

import argparse
import re
import sqlite3


def create_connection():
    """Create a database connection"""

    try:
        conn = sqlite3.connect('phones.db')
        return conn
    except sqlite3.Error as error:
        print(error)

    return None


def regexp(expr, item):
    """Regular expression function"""

    reg = re.compile(expr)
    return reg.search(item) is not None


def read_from_db(conn, argv):
    """Query rows that match the regular expression"""

    conn.create_function('REGEXP', 2, regexp)
    cur = conn.cursor()

    argv = str(argv.integer)
    phone_number_regex = argv + r'[0-9]{' + str(12 - len(argv)) + r'}$'
    cur.execute("SELECT phone_number FROM phones WHERE phone_number REGEXP ? LIMIT 10",
                (phone_number_regex,))

    rows = cur.fetchall()

    return [int(x[0]) for x in rows]


def arg_parse():
    """Initialize argument parser"""

    arg_parser = argparse.ArgumentParser(description='Process integer input')
    arg_parser.add_argument('integer',
                            type=int,
                            help='An integer input to search for a phone number')

    return arg_parser


def main():
    """Main entry point"""

    argv = arg_parse().parse_args()
    conn = create_connection()
    result = read_from_db(conn, argv)
    print(result)


if __name__ == '__main__':
    main()
