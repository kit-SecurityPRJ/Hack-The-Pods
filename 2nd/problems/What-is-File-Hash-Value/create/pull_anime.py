#!python3

import re
import sys

animes = sys.argv[1]
with open( animes, mode="r") as f:
    lines = f.readlines()

    for line in lines:
        res = re.findall("''\[\[(?:.*\|)?(.*)\]\]''", line )
        if len(res):
            print( res[0] )
