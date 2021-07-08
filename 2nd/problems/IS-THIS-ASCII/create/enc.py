#!python3
import sys

row_flag = input("flag: ")

with open( "./enc.dat", mode="wb" ) as f:
    for c in row_flag:
        f.write( bytes([ord(c)^0x80]) )
