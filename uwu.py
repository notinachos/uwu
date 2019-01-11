#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os import path
import sys

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
last_char = ''
output_text = ''

def substitute(x):
    global xmark_index

    # replace characters
    if x in xlates:
        return xlates[x]
    elif x == '!':
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

# sanity check
if len(sys.argv) < 2:
    print('usage: uwu.py filename|string')
    sys.exit(1)
else:
    text = sys.argv[1]
    if path.isfile(text):
        # input was a filename
        with open(text) as fileobj:
            for line in fileobj:
                for ch in line:
                    create_output(ch)
    else:
        # input was a sting
        #TODO: issue with create_output()/last_character 
        #      requiring this extra space.
        for i in text + ' ': 
            create_output(i)
    print(output_text)

