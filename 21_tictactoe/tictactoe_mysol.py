#!/usr/bin/env python3
"""
Author : alex <alex@localhost>
Date   : 2021-02-06
Purpose: Rock the Casbah
"""

import argparse
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-b',
                        '--board',
                        help='State of the board',
                        metavar='str',
                        type=str,
                        default=''.join('.' for i in range(1,10))
                        )

    parser.add_argument('-p',
                        '--player',
                        help='Player',
                        metavar='str',
                        type=str,
                        choices=["X","O"],
                        default=None)

    parser.add_argument('-c',
                        '--cell',
                        help='Cell',
                        metavar='int',
                        type=int,
                        default=None,
                        choices=range(1,10))

    args = parser.parse_args()
 
    x = re.findall(r'[^XO.]', args.board)
    if x or len(args.board) !=9:
        parser.error(f'--board "{args.board}" must be 9 characters of ., X, O') 

    if  args.player and not args.cell:
        parser.error('Must provide both --player and --cell')

    if args.cell and not args.player:
        parser.error('Must provide both --player and --cell')
    
    if args.player and args.cell and args.board[args.cell-1] in 'XO':
        parser.error(f'--cell "{args.cell}" already taken')

    return args  


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    board = args.board

    if args.player:
        board = board[:args.cell-1] + args.player + board[args.cell:]
    
    cells = [str(i) if c =='.' else c for i,c in enumerate(board,1)]
    
    if board == '.'*9:
        format_board('123456789')
        print('No winner.')
    else:
        if find_winner(cells):
            format_board(cells)
            print(f'{find_winner(cells)} has won!')
        else:
            format_board(cells)
            print('No winner.')


# --------------------------------------------------    
def split_chunks(seq, n):
    for i in range(0, len(seq), n):
        yield seq[i:i+n]


# --------------------------------------------------
def format_board(board):
    chunks = list(split_chunks(board,3))
    v = [' | '.join(chunk) for chunk in chunks]  # ['1 | 2 | 3', '4 | 5 | 6', '7 | 8 | 9']
    v = ['| ' + chunk + ' |' for chunk in v] 
    sep = '-------------'
    for ch in v:
        print ( sep + '\n'+ ch)
    print(sep) 
    

# --------------------------------------------------
def find_winner(board):
    wins = [('PPP......'), ('...PPP...'), ('......PPP'), ('P..P..P..'),
            ('.P..P..P.'), ('..P..P..P'), ('P...P...P'), ('..P.P.P..')]
    combos = [i for win in wins for i, j  in enumerate(win) if j == 'P'] #flat list
    wins = list(split_chunks(combos,3))
    #[[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for player in ['X','O']:
        for i, j, k in wins:
            if [board[i], board[j], board[k]] == [player, player, player]:
                return player 


# --------------------------------------------
def test_board_no_board():
    """makes default board"""
    board = """
    -------------
    | 1 | 2 | 3 |
    -------------
    | 4 | 5 | 6 |
    -------------
    | 7 | 8 | 9 |
    -------------
    """.strip()
    assert format_board('.' * 9) == board

# --------------------------------------------------
if __name__ == '__main__':
    main()
