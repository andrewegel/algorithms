#!/bin/env python

import random, sys

if len(sys.argv) < 2:
    print "Usage: %s number-of-elements" % (sys.argv[0])
    sys.exit(2)

l = range(0, int(sys.argv[1]))
random.shuffle(l)
for i in l:
    sys.stdout.write(str(i) + '\n')

sys.stdout.flush()
