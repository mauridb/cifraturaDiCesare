import os
import sys

# TODO: -read input file, -encript, 
# ex. python c_encription.py -k 5 -txt myfile.txt

alphab = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar_encript(text, key):
    # encript
    new_text = []
    for index, item in enumerate(text):
        found = alphab.index(item)
        new_index = found + key
        if new_index > 26:
            new_index = new_index %26
        print new_index
        

ARGS = sys.argv
try:
    if ARGS[1] != '-k' or ARGS[3] != '-txt':
        raise ValueError('Param errors')
    int(ARGS[2])
except ValueError as ve:
    print ve

# read input file 
with open(ARGS[4], 'r') as f:
    text = []
    for index, line in enumerate(f.readlines()):
        for char in line:
            if char.isalpha():
                text.append(char)
    caesar_encript(text, int(ARGS[2]))
