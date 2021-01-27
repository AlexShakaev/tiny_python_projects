#!/usr/bin/env python3
"""
Author : alex <alex@localhost>
Date   : 2021-01-26
Purpose: Sing bottles of bear
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    

    parser.add_argument('-n',
                        '--num',
                        help='How many bottles',
                        metavar='int',
                        type=int,
                        default=10)

    args = parser.parse_args()


    if args.num < 0:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    # verses = [verse(i) for i in range(args.num, 0, -1)]

    # print('\n\n'.join(verses))
    print('\n\n'.join(verse(i) for i in range(args.num, 0, -1)))

    

def verse(bottle):
    """Sing a verse"""
        
                
    if bottle > 2:

        a = "{} bottles of beer on the wall,".format(bottle)
        b = "{} bottles of beer,".format(bottle)
        c = 'Take one down, pass it around,'
        d = '{} bottles of beer on the wall!'.format(bottle - 1) 


        return '\n'.join([a,b,c,d])

    elif bottle == 2:
        return '\n'.join([
                    '2 bottles of beer on the wall,', '2 bottles of beer,',
                    'Take one down, pass it around,',
                    '1 bottle of beer on the wall!'
                    ])

    else:

        return '\n'.join([
                    '1 bottle of beer on the wall,', '1 bottle of beer,',
                    'Take one down, pass it around,',
                    'No more bottles of beer on the wall!'
                    ])
            

            


def test_verse():
    """Test verse"""

    last_verse = verse(1)
    assert last_verse == '\n'.join([
    '1 bottle of beer on the wall,', '1 bottle of beer,',
    'Take one down, pass it around,',
    'No more bottles of beer on the wall!'
    ])

    two_bottles = verse(2)
    assert two_bottles == '\n'.join([
    '2 bottles of beer on the wall,', '2 bottles of beer,', 
    'Take one down, pass it around,', '1 bottle of beer on the wall!'
    ])

# --------------------------------------------------
if __name__ == '__main__':
    main()
