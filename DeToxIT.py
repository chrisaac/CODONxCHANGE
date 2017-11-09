#!/usr/bin/python
import random
import sys

''' ------------------------- DeToxIT -----------------------------

    Decryption and Toxin Identification Tool

    This program is intended to provide a state-of-the-art but also
    tongue-in-cheek encrypted sequence decryptor.

    Input:     An encrypted DNA sequence.

    Output:    A roll of the dice for safe or not.

 '''

try: sequence = sys.argv[1]
except: sequence = "None"

roll = random.randrange(1,20)
if roll <= 10:
    result = "dangerous, probably"
else:
    result = "safe, probably"


print "------------- DeToxIT -------------"
print "User Input: " + str(sequence)
print "Dice Roll:  " + str(roll)
print "Result:     " + str(result)
print "\n"
