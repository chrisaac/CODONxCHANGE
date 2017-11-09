#!/usr/bin/python
import random
import sys

''' ------------------------- SeCReT -----------------------------

    Sequential Codon Reassignment Tool

    This program is intended to give you a taste of the danger
    associated with genetic recoding.

    Inputs:     Complete protein sequence in FASTA format

    Outputs:    Original sequence + mRNA
                Encrypted sequence + mRNA
                Basic statistics
 '''


# ------------------------- FUNCTIONS -----------------------------
#   generate_codons():
#   find_unique(string):
#   convert_dna(ORF, codon_table):
#   codon_tables():
#   n_switches():
#   chosen_residues():
#   minimize_codons():
#   encrypt():



'''generate_codons: generates every possible codon given the four DNA nucleotides.
   * Depends on the python 'random' library.  '''
    # TODO Can you adjust based on the GC content?
def generate_codons():
    bases, codons = ['A','T','C','G'], []
    for x in bases:
        for y in bases:
            for z in bases:
                codons.append(x + y + z)
    random.shuffle(codons)
    return codons

'''find_unique: takes a sequence and returns a string of the unique amino acids therin'''
def find_unique(string):
    return ''.join(set(string))

'''convert_dna: takes a string and uses it to create a new string via dict'''
def convert_dna(ORF, codon_table):
    sequence = ''
    for i in range(0, len(ORF), 3):
        try:
            codon = ORF[i:i+3]
            sequence += codon_table[codon]
        except KeyError:
            pass
    return sequence

'''reverse_transcribe: takes a string and uses it to create a new string via dict'''
def reverse_transcribe(ORF, codon_table):
    sequence = ''
    for i in range(0, len(ORF)):
        try:
            codon = ORF[i]
            sequence += codon_table[codon]
        except KeyError:
            pass
    return sequence

'''codon_tables: basically clears up the clutter of the other functions'''
def codon_tables():
    universal_code = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
        'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
        }

    NtoP_code = {
        'ATT':'I', 'CTT':'L', 'GTT':'V', 'TTT':'F',
        'ATG':'M', 'TGT':'C', 'GGT':'G', 'CCT':'P',
        'ACT':'T', 'TCT':'S', 'TAT':'Y', 'TGG':'W',
        'CAA':'Q', 'AAT':'N', 'CAT':'H', 'GAA':'E',
        'GAT':'D', 'AAA':'K', 'CGT':'R', 'GCA':'A',
        'TAA':'*'
        }

    PtoN_code = {
        'I':'ATT', 'L':'CTT', 'V':'GTT', 'F':'TTT',
        'M':'ATG', 'C':'TGT', 'G':'GGT', 'P':'CCT',
        'T':'ACT', 'S':'TCT', 'Y':'TAT', 'W':'TGG',
        'Q':'CAA', 'N':'AAT', 'H':'CAT', 'E':'GAA',
        'D':'GAT', 'K':'AAA', 'R':'CGT', 'A':'GCA',
        '*':'TAA'
        }

    return (universal_code, NtoP_code, PtoN_code)

''' n_switches: '''
def n_switches(sequence):
    return int(random.randint(1,len(find_unique(sequence))))

''' chosen_residues: '''
def chosen_residues(sequence):
    #Initialization
    switches = n_switches(sequence)
    chosen, unique = [], list(find_unique(sequence))
    random.shuffle(unique)

    #Operation
    for n in range(switches):
        chosen.append(unique.pop())
    return chosen

''' minimize_codons: '''
def minimize_codons(NtoP_code):
    codons = generate_codons()
    for n in NtoP_code.keys():
        codons.remove(n)
    random.shuffle(codons)
    return codons

''' encrypt: '''
def encrypt(sequence, chosen, codons):
    seen = {} #Which codons have been assigned
    encrypted = [] #The final sequence to be returned

    for n in sequence:
        if n not in seen:
            if n in chosen:
                seen[n] = codons.pop()
                encrypted.append(seen[n])
            else:
                seen[n] = PtoN_code[n]
                encrypted.append(seen[n])
        else:
            encrypted.append(seen[n])

    #Final step and concatenation
    return "".join(encrypted)

# ------------------------ USER INPUTS ----------------------------

try: sequence = str(sys.argv[1])
except:
    sequence = 'MMVRKRHKDESTNQCGPAVILMYWRMVSM'
    print "Running in Test Mode..."

# REMOVED OTHER OPTIONS

# ------------------------- CODE BODY -----------------------------

# Stores useful codon tables into memory
universal_code, NtoP_code, PtoN_code = codon_tables()
# Picks randomly a few residues from a sequence
chosen = chosen_residues(sequence)
# Reduces available codons to non-conflicting set
codons = minimize_codons(NtoP_code)
# Encrypt the sequence provided by the user
encrypted_sequence = encrypt(sequence, chosen, codons)

# ------------------------- OUTPUTS -----------------------------

print "-------------- SeCReT --------------"
print "Number of Recodings: " + str(len(chosen))
print "Chosen Residues:     " + str("".join(chosen))
print ""
print "-------------- Results -------------"
print "User Input: " + str(sequence)
print "Encrypted:  " + str(convert_dna(encrypted_sequence, universal_code))
print ""
print "User DNA:   " + str(reverse_transcribe(sequence, PtoN_code))
print "Encrypted:  " + str(encrypted_sequence)
print ""
