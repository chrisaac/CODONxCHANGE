# CODONxCHANGE
Bioinformatics software to test the limits of genetic recoding and biosecurity.
This software was developed for the 2017 Lethbridge iGEM Team and consists of three tools:
1. GRecoS
2. SeCReT
3. DeToxIT

All tools are written in Python 2.7 and run from the command line. 
First make sure that you have Python installed to your machine.
Instructions can be found at: [Python.org](https://www.python.org/)

To use the tools, navigate to the source directory and input the following command:
```
python TOOLNAME.py
```
This will run the tool with default values. 
Additional input parameters are specific for each tool and are discussed below.

## GRecoS
### Genetic Recoding Space
This tool is designed to calculate the extremely large number of possible genetic codes that exist for different biological parameters made possible by genetic recoding.
The software is also able to calculate genetic codes made possible with additional bases, more amino acids, or alternative lengths of codons. 
Following user input, the tool returns the lower and upper estimates of the sample space.

Usage:
```
python GRecoS.py <number of nucleotides> <length of codon> <number of amino acids>
```

## SeCReT
### Sequential Codon Reassignment Tool
This tool takes a user-provided protein sequence and randomly chooses some number of amino acids to recode.
These chosen amino acids are then randomly assigned an unused codon that is intended to correspond to a mutant or misacylated tRNA.
The original protein, its encrypted version, and the corresponding DNA sequences are returned.

Usage:
```
python TOOLNAME.py <input protein sequence>
```

## DeToxIT
### Decryption and Toxin Identification Tool
Encryption is easy, and decryption is hard. Though we believe this problem will ultimately be solvable, it remains to be seen just how this can be done given the immense combinatorial search space. 
As a bit of a joke, this state of the art tool flips a coin to determine whether or not a provided sequence is safe of not. 
Sad as it is, this tool is the first to address this problem, and represents the state of the art.
We believe that genetic recoding and DNA encryption is a real and troubling problem for the future, and will be continuing to try to find solutions.

Usage:
```
python TOOLNAME.py <input DNA or protein sequence> 
```

Learn more about our project, [Next Vivo](http://2017.igem.org/Team:Lethbridge) on our wiki! 
