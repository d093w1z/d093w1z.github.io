#!/usr/bin/python3
import sys
from os import system
cmd = [
    'sed s/";"/";\\n"/g',
    'sed s/"}"/"}\\n"/g'
]
system("cat "+sys.argv[1]+"|"+"|".join(cmd)+">output.js")

