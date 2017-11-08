#!/usr/bin/python
import sys
import math

# --- GRecoS ---
# Genetic Recoding Space
# Estimates the lower bound of the potential number of genetic codes.

'''sample_space: takes basic biological parameters and returns the number of possible genetic codes'''
def sample_space(n_bases, l_codon, n_aminos):
    n_codons = int(n_bases)**int(l_codon)
    n_choose_a = (math.factorial(int(n_codons)))/((math.factorial(int(n_aminos)))
*(math.factorial(int(n_codons-n_aminos))))

    n_tables = int(n_choose_a)*math.factorial(n_aminos)
    print "There are %s possible codons utilizing %s bases in groups of %s" % (n_codons, n_bases, l_codon)
    print "%s possible genetic codes exist when %s amino acids are required" % (n_tables, n_aminos)

try: a = int(sys.argv[1])    # Defines the amount of nucleic acids available to a sequence,
except: a = int(4)           # All conventional DNA or RNA bases: ATCG or AUCG.

try: b = int(sys.argv[2])    # Defines the length of the codon read by a ribosome.
except: b = int(3)           # Codons are 3 bases long.

try: c = int(sys.argv[3])    # Defines the number of amino acids in the system. Related to codon degeneracy.
except: c = int(20)         # All essential amino aicds are needed.

print ""
sample_space(a, b, c)
