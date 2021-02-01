#!/usr/bin/env python3
"""
Author : alex <alex@localhost>
Date   : 2021-01-31
Purpose: Rock the Casbah
"""

import argparse
import re 
import string
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Southern fry text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    # text = args.text 

    for line in args.text.splitlines():
       
        words = []
        for word in re.split(r'(\W+)', line.rstrip()):
            first = friar(word)
            if first!=word:
                words.append(first + "in'")
            else:
                words.append(word)

        t = []
        for word in words:
            t += yall(word)
        print(''.join(t))

# --------------------------------------------------

def friar(word):
    
    pattern = (
        r'(\w+)'
        '(ing$)'
    )
    p = re.compile(pattern)
    match = p.search(word) 

    vowel_pattern = ('[aeiouAEIOU]')
    v = re.compile(vowel_pattern)
    if match and v.search(match.group(1)):
        first = p.search(word).group(1) 
    else: 
        first = word 
    return first
    
# --------------------------------------------------

def yall(word):
    pattern = (      
        '(^you$|^You$)'                          
    )
    p = re.compile(pattern)
    match = p.search(word)
    y = p.search(word).group() if match else ""

    if y=='you':
        w = "y'all"
    elif y == "You":
        w = "Y'all"
    else:
        w = word
    return w 

#---------------------------------------------------
def test_friar():
    
   
    assert friar('fishing') == "fish"
    assert friar('Aching') == "Ach" 
    assert friar('swing') == 'swing'
        
# --------------------------------------------------
if __name__ == '__main__':
    main()
