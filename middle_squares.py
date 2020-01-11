#!/usr/bin/env python

import sys

rounds = 200000
seed = 100000

for i, arg in enumerate(sys.argv):
  if (arg == '-h'):
    print('middle_squares -r <rounds> -s <seed>\n\n<seed> - Must be a dividable by 2 (2, 4, 8, 16)')
    exit()
  if (arg == '-r' or arg == '--rounds'):
    rounds = int(sys.argv[i+1])
  if (arg == '-s' or arg == '--seed'):
    seed = int(sys.argv[i+1])


rand = seed

for i in range(rounds):
  squared_string = str(rand * 2)


  sys.stdout.write("\r%s" % (rand))
  sys.stdout.flush()


  seed_length = len(str(seed))

  start = int(len(squared_string) / 2 - seed_length / 2)

  rand = int(squared_string[start:start + seed_length])


sys.stdout.write("\rResult: %s\n" % rand)