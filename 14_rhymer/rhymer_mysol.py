#!/usr/bin/env python3
"""
Author : alex <alex@localhost>
Date   : 2021-01-30
Purpose: Make rhyming "words"
"""

import argparse
import string as s
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        type = str,
                        help='A word to rhyme')

    args = parser.parse_args()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word

    cons_clusters = 'bl br ch cl cr dr fl fr gl gr pl pr sc sh sk sl sm sn sp st \
        sw th tr tw thw wh wr sch scr shr sph spl spr squ str thr'
    c = cons_clusters.split()


    consonants = ''.join([c for c in s.ascii_lowercase if c not in 'aeiou'])

    c.extend(list(consonants))
    
    def create_output():
        output = [x+last for x in c]
        out = sorted(output)
        o = '\n'.join(out)
        print(o)

    if stemmer(word) !=(word.lower(), ''):
        first, last = stemmer(word)
        if first =='': 
            create_output()    
        else:
            index = c.index(first)   
            c.pop(index)
            create_output()
            
    else:
        print(f'Cannot rhyme "{word}"')


    # print(stemmer(word))

    
# --------------------------------------------------
def stemmer(word):
    """Return leading consonants (if any), and 'stem' of word"""
    # consonants = [c for c in s.ascii_letters if c not in 'aeiou'] pattern must be str, not list
    consonants = ''.join([c for c in s.ascii_lowercase if c not in 'aeiou'])
    
    pattern = f'([{consonants}]+)?([aieou])(.*)'

    match = re.match(pattern, word.lower())
    
    if match:
        p1 = match.group(1) or '' #to ensure we don't return any None values
        p2 = match.group(2) or ''
        p3 = match.group(3) or ''
        return (p1, p2 + p3)
    else:
        return (word.lower(), '')

# --------------------------------------------------
def test_stemmer():
    """ Test stemmer"""
    assert stemmer("") == ("", "")
    assert stemmer('cake') == ('c', 'ake')
    assert stemmer('chair') == ('ch', 'air') 
    assert stemmer('APPLE') == ('', 'apple')
    assert stemmer('RDNZL') == ('rdnzl', '') 
    assert stemmer('123') == ('123', '')

# --------------------------------------------------
if __name__ == '__main__':
    main()
