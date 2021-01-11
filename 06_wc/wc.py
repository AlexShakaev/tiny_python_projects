#!/usr/bin/env python3 
"""
Author : alex <alex@localhost>
Date   : 2020-12-06
Purpose: Rock the Casbah
"""

import argparse
import io
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file', metavar="FILE",
                        nargs='*', 
                        type = argparse.FileType('rt'),
                        default=[sys.stdin],
                        help='Input file(s)')

    

    


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(args)
    
    # num_lines = 0
    # num_words = 0
    # num_bytes = len(num_words)*len(num_lines)
    # for file in args:
    #     if os.path.isfile(file):
    #         fh = open(file)
    #         for line in fh:
    #             num_lines+=1
    #             for word in line:
    #                 num_words+=1
    #     else:
    #         print("No such file")         
    # if not num_lines:
    #     print('File is empty')       
    # else:
    #     print("{:8} {:8} {:8}".format(num_lines, 
    #                     num_words, num_bytes))


# --------------------------------------------------
if __name__ == '__main__':
    main()
