#!/usr/bin/python
import sys
import math

# --- GRecoS ---
# Genetic Recoding Space
# Estimates the lower bound of the potential number of genetic codes.

'''nCr: calculates the combinations for n choose r'''
def ncr(n, r):
    try:
        value = math.factorial(int(n)) / (math.factorial(int(r))*math.factorial(int(n-r)))
    except ValueError:
        print "Invalid Parameters: n^l must be greater than a"
        value = 0
    return int(value)

'''lower_space: returns the number of possible genetic codes for biological parameters'''
def lower_space(n_bases, l_codon, n_aminos):
    n_codons = n_bases**l_codon
    n_choose_a = ncr(n_codons, n_aminos)
    n_tables = n_choose_a*math.factorial(n_aminos)
    print "Lower Bound Equations"
    print n_tables

'''upper_space: estimates (slightly overcounting) the maximum genetic codes '''
def upper_space(n_bases, l_codon, n_aminos):
    nl = n_bases**l_codon
    value = 0
    for i in range(n_aminos, nl):
        value += ncr(nl, i) * ncr(i, n_aminos) * math.factorial(n_aminos) * n_aminos**(i-n_aminos)
    print "Upper Bound Equation"
    print value


# --- USER INPUT SECTION ---

try: a = int(sys.argv[1])    # Defines the amount of nucleic acids available to a sequence,
except: a = int(4)           # All conventional DNA or RNA bases: ATCG or AUCG.

try: b = int(sys.argv[2])    # Defines the length of the codon read by a ribosome.
except: b = int(3)           # Codons are 3 bases long.

try: c = int(sys.argv[3])    # Defines the number of amino acids in the system. Related to codon degeneracy.
except: c = int(20)         # All essential amino aicds are needed.


# --- Awesome Stuff ---

print "------------- GRecoS -------------"
print "Number of Nucleic Acids: " + str(a)
print "Length of the Codon:     " + str(b)
print "Number of Unique Codons: " + str(a**b)
print "Number Amino Acids:      " + str(c)
print "\n"
print "------------- Results -------------"
upper_space(int(a), int(b), int(c))
lower_space(int(a), int(b), int(c))
print "\n"
