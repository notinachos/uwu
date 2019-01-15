#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
from os import path

""" 
Inspired by a CraigsList ad.

Basic Usage:
    ./uwu.py "your string looks silly"
    youw stwing wooks siwwy

Can also be used on text files:
    uwu.py test.txt
"""

# characters to replace
xlates = {
    'n':'ny',
    'N':'Ny',
    'l':'w',
    'L':'W',
    'r':'w',
    'R':'W'}

# lookahead characters
# (if the next letter is one of these, don't substitue)
lookahead = [
    ' ',
    '\n',
    'd','D',
    't','T',
    'g','G']

# replace exclamation marks with faces
xmarks = [
    ' ;;w;; ',
    ' (・`ω´・) ',
    ' >w< ',
    ' UwU ']

xmark_index = 0
xlate_count = 0
last_char = ''
output_text = ''

def substitute(x):
    global xmark_index
    global xlate_count
    # replace characters
    if x in xlates:
        xlate_count += 1
        return xlates[x]
    elif x == '!':
        xlate_count += 1
        return xmarks[xmark_index]

    # cycle faces every new paragraph (2x \n)
    elif x == '\n':
        if len(output_text) > 0:
            if output_text[-1] == '\n':
                xmark_index = xmark_index + 1
                if xmark_index == len(xmarks):
                    xmark_index = 0
        return '\n'

    # no substitution
    else:
        return x

def create_output(character):
    global output_text
    global last_char
    if character in lookahead:
        # handle edge cases
        if last_char == '!':
            output_text = output_text + substitute(last_char)
        elif last_char == 'r' or last_char == 'R':
            output_text = output_text + substitute(last_char)
        elif character == '\n' and last_char == 'n' or last_char == 'N':
            output_text = output_text + last_char
        elif character == ' ' and last_char == 'n' or last_char == 'N':
            output_text = output_text + last_char
        elif last_char == 'l' or last_char == 'L':
            output_text = output_text + substitute(last_char)
        elif last_char == 'r' or last_char == 'R':
            output_text = output_text + substitute(last_char)
        else:
            output_text = output_text + last_char
    else:
        output_text = output_text + substitute(last_char)
    last_char = character


if __name__ == '__main__':
    # define command line arguments
    parser = argparse.ArgumentParser(
        description='A script for making text sillier.'
    )
    parser.add_argument(
        'text',
        help='text or file to translate. '
             'input can either be double quoted text or a filename. '
    )
    parser.add_argument(
        '-c',
        '--count',
        help='do not translate. instead, return the number of translations the script would have made.',
        action='store_true'
    )

    # parse command line arguments
    args = parser.parse_args()

    # input was a file
    if path.isfile(args.text):
        with open(args.text) as fileobj:
            for line in fileobj:
                for ch in line:
                    create_output(ch)
    # input was a string
    else:
        #TODO: issue with create_output()/last_character 
        #      requiring this extra space.
        for i in args.text + ' ': 
            create_output(i)
    
    # display results
    if args.count:
        print(xlate_count)
    else:
        print(output_text)
