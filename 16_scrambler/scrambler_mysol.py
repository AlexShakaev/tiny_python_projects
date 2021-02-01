#!/usr/bin/env python3
"""
Author : alex <alex@localhost>
Date   : 2021-02-01
Purpose: Scramble the letters of words
"""

import argparse
import random
import os
import re
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Scramble the letters of words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')


    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    args =  parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    random.seed(args.seed)
    pattern = "([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)"
    splitter = re.compile(pattern)

    for line in args.text.splitlines():
        output = []
        for word in splitter.split(line):
            output.append(scramble(word))

        print(''.join(output))


# --------------------------------------------------
def scramble(word):
    """Scramble a word"""
    
    punc_pattern = '[!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]'
    match = re.search(punc_pattern, word)
    if match and len(word) < 3:
        return word
    if len(word) < 4:
        return word
    else:
        
     
        middle = list(word[1:-1])
        random.shuffle(middle)
        return word[0] + ''.join(middle) + word[-1]     


# --------------------------------------------------
def test_scramble():
    state = random.getstate()
    random.seed(1)
    assert scramble('a') == 'a'
    assert scramble("ab") == "ab"
    assert scramble("abc") == "abc" #words with three chars of fewer should be returned unchanged
    assert scramble("abcd") == "acbd"
    assert scramble("abcde") == "acbde"
    assert scramble("abcdef") == "aecbdf"
    assert scramble("abcde'f") == "abcd'ef"
    random.setstate(state)


# --------------------------------------------------
if __name__ == '__main__':
    main()
