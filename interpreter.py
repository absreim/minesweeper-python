# Text-based command interpreter for the game

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('rows', 'Number of rows in the game board')
parser.add_argument('cols', 'Number of columns in the game board')
parser.add_argument('mines', 'Number of mines')
parser.parse_args()
