#!/usr/bin/env python3
"""nargs = + """

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="nargs = +", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "items", metavar="str", nargs="+", type=str, help="A positional argument"
    )

    # parser.add_argument('-s',
    #                     '--sorted',
    #                     help='sorted args',
    #                     metavar='str',
    #                     type=str,
    #                     default='')

    # parser.add_argument('-i',
    #                     '--int',
    #                     help='A named integer argument',
    #                     metavar='int',
    #                     type=int,
    #                     default=0)

    # parser.add_argument('-f',
    #                     '--file',
    #                     help='A readable file',
    #                     metavar='FILE',
    #                     type=argparse.FileType('rt'),
    #                     default=None)

    parser.add_argument("-s", "--sorted", help="A boolean flag", action="store_true")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """main"""

    args = get_args()
    list = args.items
    template = "You are bringing"
    # print(args.sorted)
    # print(list)
    if args.sorted:
        list = sorted(list)
    # print(list)

    if len(list) == 1:
        print(template + f" {list[0]}.")
    elif len(list) == 2:
        print(template + f" {list[0]} and {list[1]}.")
    else:
        print(template + f" {', '.join(list[:-1])}, and {list[-1]}.")
    # str_arg = args.arg
    # int_arg = args.int
    # file_arg = args.file
    # flag_arg = args.on
    # pos_arg = args.positional

    # print(f'str_arg = "{str_arg}"')
    # print(f'int_arg = "{int_arg}"')
    # print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    # print(f'flag_arg = "{flag_arg}"')
    # print(f'positional = "{pos_arg}"')


# --------------------------------------------------
if __name__ == "__main__":
    main()
