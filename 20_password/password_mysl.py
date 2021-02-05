#!/usr/bin/env python3
"""
Author : alex <alex@localhost>
Date   : 2021-02-05
Purpose: Password maker
"""

import argparse
import random
import re
import string

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Password maker',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        
                        metavar='FILE',
                        nargs='+',
                        help='Input file(s)',
                        type=argparse.FileType('rt'))

    parser.add_argument('-n',
                        '--num',
                        help='Number of passwords to generate ',
                        metavar='num_passwords',
                        type=int,
                        default=3)

    parser.add_argument('-w',
                        '--num_words',
                        help='Number of words to use for password',
                        metavar='num_words',
                        type=int,
                        default=4)

    parser.add_argument('-m',
                        '--min_word_len',
                        help='Minimum word length',
                        metavar='minimum',
                        type=int,
                        default=3)
    
    parser.add_argument('-x',
                        '--max_word_len',
                        help='Maximum word length ',
                        metavar='maximum',
                        type=int,
                        default=6)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)


    parser.add_argument('-l',
                        '--l33t',
                        help='Obfuscate letters',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    words = set()

    def word_len(word):
        return args.min_word_len <= len(word) <= args.max_word_len

    for fh in args.file:
        for line in fh:
            for word in filter(word_len, map(clean, line.lower().split())):
                words.add(word.title())
    words  = sorted(words)

    passwords = [''.join(random.sample(words, args.num_words)) for _ in range(args.num)]

    print('\n'.join(passwords) if not args.l33t else '\n'.join(map(l33t,passwords)))
    

# --------------------------------------------------
def clean(word):
    return re.sub('[^A-Za-z0-9]', '', word)


# -------------------------------------------------
def ransom(word):
    return ''.join(char.upper() if random.choice([0, 1]) else char.lower() for char in word)


# -------------------------------------------------
def l33t(word):
    jumper =  { 'a': '@', 
                'A' : '4', 
                'O' : '0',
                't' : '+',
                'E' : '3',
                'I' : '1',
                'S' : '5'}
    return ''.join([jumper.get(char, char) for char in ransom(word)]) \
                                  + random.choice(string.punctuation)


# -------------------------------------------------
def test_l33t():
    state = random.getstate()
    random.seed(1)
    assert l33t('Money') == 'moNeY{'
    assert l33t('Dollars') == 'D0ll4r5`'
    random.setstate(state)


# -------------------------------------------------
def test_ransom():
    state = random.getstate()
    random.seed(1)
    assert ransom('Money') == 'moNeY'
    assert ransom('Dollars') == 'DOLlaRs'
    random.setstate(state)


# --------------------------------------------------
def test_clean():
    assert clean('') == ''
    assert clean("states,") == 'states'
    assert clean("Don't") == 'Dont'


# --------------------------------------------------
if __name__ == '__main__':
    main()
