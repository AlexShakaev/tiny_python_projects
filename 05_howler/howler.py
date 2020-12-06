#!/usr/bin/env python3
"""
Author : alex <alex@localhost>
Date   : 2020-12-05
Purpose: Rock the Casbah
"""

import argparse
import os
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Howler (upper-cases input)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="str", help="Input string or file", type=str)

    parser.add_argument(
        "-o", "--outfile", help="Output file", metavar="str", type=str, default=""
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    # print(args)
    def read_text():
        if os.path.isfile(args.text):
            file_ = open(args.text).read().rstrip()
            return file_.upper()
        else:

            return args.text.upper().rstrip()

    if args.outfile:
        if os.path.isfile(args.outfile):

            out_file = open(args.outfile, "at")
            t = read_text()
            out_file.write(t + "\n")
            # print(read_text(), file = out_file)
            out_file.close()
        else:
            out_file = open(args.outfile, "wt")
            out_file.write(read_text() + "\n")
            # print(read_text(), file = out_file)
            out_file.close
    else:
        print(read_text())


# --------------------------------------------------
if __name__ == "__main__":
    main()
