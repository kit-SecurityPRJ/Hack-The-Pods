#!python3
import sys

with open("./flag.dat", mode="rb" ) as f:
    row_flag = f.read()

with open( "./result.dat", mode="wb" ) as f:
    for c in row_flag:
        f.write( bytes([c^0x80]) )
