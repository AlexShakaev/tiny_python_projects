#!/usr/bin/env python3


"""
Author : alex <alex@localhost>
Date   : 2020-12-04
Purpose: Jump it
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Jump the five",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="str", nargs="+", help="Input text")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jump  here"""

    args = get_args()
    text = args.text

    # print(args)
    text = ' '.join(args.text)
    # print(text)

    # str_nums = [str(i) for i in range(0,10)]
    # phone_number = [int(sub_arg) for arg in text
    # 			  for sub_arg in arg
    #                     if sub_arg in str_nums]
    # print(phone_number)

    l = list(zip(reversed(range(10)), range(1, 10)))
    crypto_dict = dict(l)
    crypto_dict.update({0: 5, 5: 0})

    

    crypto_dict = {str(k):str(v) for k,v
       in crypto_dict.items()}
    # print(crypto_dict)
    z = [crypto_dict[char] if char in crypto_dict else char for char in text if 
	 char in text]
    # print(z) 
    print(''.join(z))


if __name__ == "__main__":
    main()
