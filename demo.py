#! /usr/bin/env python
import sys

# Read list of numbers
numbers = [float(line) for line in open(sys.argv[1])]
n_bins = len(numbers)/12

# Print lists of numbers, labeled 'b'
for i in range(n_bins):
    print 'b', ' '.join(map(str, numbers[i*12:(i+1)*12]))
