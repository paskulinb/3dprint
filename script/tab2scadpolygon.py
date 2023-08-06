#!/usr/bin/python3

import sys
import re

points = []

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        m = re.match('(-*[\d\\.]+)\s+(-*[\d\\.]+)', line)   #parse coord: "142.3455 -23.41"
        if (m):
            points.append( "[" + m.group(1) + "," + m.group(2) + "]")

print ('[' + ','.join(points) + ']')
