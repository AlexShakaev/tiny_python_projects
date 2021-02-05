#!/usr/bin/env python3
"""
Author : alex <alex@localhost>
Date   : 2021-02-04
Purpose: Create Workout Of (the) Day (WOD)
"""

import argparse
import io
import random
import re 
import csv
from pprint import pprint
from tabulate import tabulate


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create Workout Of (the) Day (WOD)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-n',
                        '--num',
                        help='Number of exercises',
                        metavar='exercises',
                        type=int,
                        default=4)

    parser.add_argument('-f',
                        '--file',
                        help='CSV input file of exercises',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='inputs/exercises.csv')

    parser.add_argument('-e',
                        '--easy',
                        help='Halve the reps',
                        action='store_true')

    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    exercises = read_csv(args.file)
    output = []
    for ex, low, high in random.sample(exercises,  k = args.num):
        n = random.randint(low, high)
        n = int(n/2) if args.easy else int(n) 
        output.append((ex, n))
    
    
    print(tabulate(output, headers=('Exercise', 'Reps')))


# --------------------------------------------------
def read_csv(fh):
    """ Read the csv input"""
    reader = csv.DictReader(fh, delimiter=',')
    exercises = []
    
    for rec in reader:
        name, reps = rec['exercise'], rec['reps']
        low, high = map(int, reps.split('-'))
        # number = random.randint(low, high)
        exercises.append((name, low, high))

    return exercises


# --------------------------------------------------
def test_read_csv():
    """Test read_csv"""
    text = io.StringIO('exercise,reps\nBurpees,20-50\nSitups,40-100')
    assert read_csv(text) == [('Burpees', 20, 50), ('Situps', 40, 100)]

    

# --------------------------------------------------
if __name__ == '__main__':
    main()
