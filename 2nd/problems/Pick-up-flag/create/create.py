#!python3

import random

ascii = [ chr(c) for c in range( 0x21, 0x7f ) if c != 0x5c ]

for i in range( 10000 ):
    print( random.choice( ascii ), end='' )

# inject the flag with notepad.
