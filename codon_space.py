#!/usr/bin/python
import sys
import math

'''sample_space: takes basic biological parameters and returns the number of possible genetic codes'''
def sample_space(n_switches, n_aminos, n_bases, l_codon):
    n_codons = int(n_bases)**int(l_codon)
    n_tables = (math.factorial(int(n_codons)) / math.factorial(int(n_codons) - int(n_switches))) / math.factorial(int(n_aminos))
    print "There are %s possible codons utilizing %s bases in groups of %s" % (n_codons, n_bases, l_codon)
    print "There are %s possible genetic codes exist when %s amino acids are required" % (n_tables, n_aminos)

try: a = sys.argv[1]    # Definies the number of switches
except: a = 64          # Complete recoding of the table. Everything is switched.

try: b = sys.argv[2]    # Defines the number of amino acids in the system. Related to codon degeneracy.
except: b = 20          # All essential amino aicds are needed.

try: c = sys.argv[3]    # Defines the amount of nucleic acids available to a sequence,
except: c = 4           # All conventional DNA or RNA bases: ATCG or AUCG.

try: d = sys.argv[4]    # Defines the length of the codon read by a ribosome.
except: d = 3           # Codons are 3 bases long.

sample_space(a, b, c, d)
