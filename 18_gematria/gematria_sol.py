#!/usr/bin/env python3
"""
Author : alex <alex@localhost>
Date   : 2021-02-03
Purpose: Rock the Casbah
"""

import argparse
import os
import string
import re 


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gematria',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')
    
    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args 


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text

    for line in text.splitlines():
        values = []
        for word in line.split():
            val = word2num(word)
            values.append(val)
            
        print(" ".join(values))
    

# --------------------------------------------------
def word2num(word):
    

    w = re.sub('[^A-Za-z0-9]', '', word)
    s = sum(map(ord, w))
    return str(s)
    # return (' '.join(str(ord(letter)) for letter in w))
    

# --------------------------------------------------
def test_word2num():
    """Test word2num"""
    assert word2num("a") == "97"
    assert word2num("abc") == "294"
    assert word2num("ab'c") == "294"
    assert word2num("4a-b'c,") == "346"


# --------------------------------------------------
if __name__ == '__main__':
    main()
