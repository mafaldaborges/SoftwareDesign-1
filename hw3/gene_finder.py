# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 4:06:42 2014

@author: Mafalda Borges
"""
from load import load_seq
#dna = load_seq("./data/X73525.fa")
# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons

def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    
    # expand the list of dna into all values
    sequence = list(dna)
    #find length of list so it can be divided 3 to tell us the number of amino acids
    length = len(sequence)
    #divide length by three
    length = length/3
    #blank list to put the amino acids in
    codon_list = []
    amino_acid_string=''
    #the for loop to go through the codons

    for b in range (length):	#If this is all you are planning to use sequence and length for,
    							# don't create them as variables, just make a for statement with
    							# b in range(len(dna)/3). Len works on strings. Also, rather than
    							# dividing your length by 3, and then multiplying each iteration by 3,
    							# you can just increment your for loop by 3 each time by
    							# using the third argument of range so that your for loop reads
    							# "for b in range(0,len(dna),3):"
        start = 3*b
        stop = 3*b + 3
        #b is used to say where the codons start and stop
        codon_list.append(dna[start:stop]) #codon_list is a list of codons (so dna nucleotides in sets of three)
        for index in range (len(codons)): 
            if codon_list[b] in codons[index]: #searches the list of dna triplets to see if triplet exists in it which it should
                amino_acid_string += (aa[index]) #adds corresponding amino acid to list
    return amino_acid_string
    
    #print amino_acid_list                    
                    
                    
                    


def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
        
    print 'input: ATCGACGTACG, output: IDV, ' + coding_strand_to_AA('ATCGACGTACG')
    print 'input: TGCAATCGAAA, output: CNR, ' + coding_strand_to_AA('TGCAATCGAAA')
    # YOUR IMPLEMENTATION HERE

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    
    #This function is bugged! My unit tests show that you're forgetting to reverse the string:
    #input: ATGCCCGCTTT, expected output: AAAGCGGGCAT , actual output: TACGGGCGAAA
	#input: CCGCGTTCA, expected output: TGAACGCGG , actual output: GGCGCAAGT

    length = len(dna) #finds length of DNA for range
    reverse_string = '' #creating an open string to add to
    
    for b in range(length):
        if dna[b] == 'A':
            reverse_string +=('T') #adds T to reverse string if input A
        elif dna[b] == 'T':
            reverse_string +=('A')#adds A to reverse string if input T 
        elif dna[b] == 'C':
            reverse_string +=('G')#adds G to reverse string if input C
        elif dna[b] == 'G':
            reverse_string +=('C')#adds C to reverse string if input G
    return reverse_string
    	#The reverse_string is never reversed here. Try "return reverse_string[::-1]".
    #print reverse_string

        
def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
        
    print 'input: TGCATTCAT, expected output: ACGTAAGTA, output:', get_reverse_complement('TGCATTCAT')
        
def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    
    #This function is bugged! Your code is truncating the letters on the end that are not part of a full codon.
    #input: ATGGGGAGCTTGA, expected output: ATGGGGAGCTTGA, actual output: ATGGGGAGCTTG


    #start codon is ATG
    
    #add length of codon to start
    
    codons = [None]*int(len(dna)/3) #creating a list for codons
    # Hmm. So preallocation is a fine idea, and you're doing it correctly,
    # but honestly, the time you save is on the order of microseconds
    # at this scale (Python is alot better at list allocation than
	# than MATLAB). Well done, but also probably not necessary.

	# Also, fun fact - I assume you cast to an int because you came
	# up with a float otherwise. Another way to do this would be to 
	# use the // operator which forces python to return an integer
	# result (but always floors the rounded number EG. 7.7//2 = 3.0).

    ORF = [] #creating an empty list for open reading frames.
    for b in range (int(len(dna)/3)):
        codons[b] = dna[b*3:b*3+3] #telling code to read in groups of 3 (there are 3 nucleotides in a codon)
        		#I believe that chunking data like this is what is generating your bug.
        if codons[b] == 'TAG' or codons[b] == 'TAA' or codons[b] == 'TGA': #telling the strand to end if stop codon is reached
        								#Just fyi, another way to do this would be "if codons[b] in ['TAG','TAA','TGA']:"
            break
        else:
            ORF.append(codons[b])#adding codons to codon list
    output_ORF = ''.join(ORF) #creating a string for the output
    return output_ORF
    
    

    

def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
    
    print rest_of_ORF('ATGAATATGAATGATTAAGATATAAGGTAA')
        
    print 'input: ATGAATGATTAA, output ATGAATGAT', rest_of_ORF('ATGAATGATTAA')
    print 'input: ATGAATGATATAAGGTAA, output ATGAATGATATAAGG', rest_of_ORF('ATGAATGATATAAGGTAA')
        
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """

    #This function is bugged too as a result of the bug in rest_of_ORF(). But its only counted for grading purposes once.
    #input: ATGCATGAATGTAGATAGATGTGCCC, expected output: ['ATGCATGAATGTAGA', 'ATGTGCCC'] , actual output: ['ATGCATGAATGTAGA', 'ATGTGC']
	#input: ATGTGCATGAGATAGGATGGGATGCTTG, expected output: ['ATGTGCATGAGA', 'ATGCTTG'], actual output: ['ATGTGCATGAGA', 'ATGCTT']

    #sequence = 'TCATGAGGCTTTGGTAAATAT'
    # start by reading only from [3*n: 3*n +3]
    # while n < length(dna/3)
    #if something = ATG
    #then add other letters to the list
    #how to ignore other uses of ATG
    #use the previous program to add list
    #how to get it to loop again
    
   #control n (output of function becomes new n)
    orf_list = [] #creating an empty list to add to
    n = 0 #n is used for indexing so we start at 0
    while n <= (len(dna)):
        index = 3*n #telling program to read in groups of three
        if dna[index:index+3] == 'ATG': #telling it to start reading at ATG
            string_of_orf = rest_of_ORF(dna[index:len(dna)]) 
            orf_list.append(string_of_orf) #adds sequence of gene to list
            n = n + len(string_of_orf)/3 #updates value of n
        else:
            n += 1 #changes value of n if ATG is not found
    return orf_list
            

     
    # YOUR IMPLEMENTATION HERE        
     
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """
    print 'input AATGAAATGGATCCCTTTTAACCCGGGATGCCCGGGTAA, output [ATGGATCCCTTT, ATGCCCGGG]', find_all_ORFs_oneframe('AATGAAATGGATATGTAGCCCTTTTAACCCGGGATGCCCGGGTAA')

    # YOUR IMPLEMENTATION HERE

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    #print dna
    half_the_codons = [] #sets open list for half the codons since we are not using the reverse string of DNA
    for i in range(0,3): # i = 0, i = 1, i = 2
        half_the_codons += find_all_ORFs_oneframe(dna[i:]) #uses offsets to find all the codons for one strand of DNA
    
#    print half_the_codons
    return half_the_codons
        
         
    # YOUR IMPLEMENTATION HERE

def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
        
    print 'input AATGAAATGGATCCCTTTTAACCCGGGATGCCCGGGTAA, output [ATGGATCCCTTT, ATGCCCGGG, ATGAAATGGATCCCTTTTAACCCGGGATGCCCGGGT]' + find_all_ORFs('AATGAAATGGATCCCTTTTAACCCGGGATGCCCGGGTAA')

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """

    #This function is bugged as well, but I believe this is a result of the cascading bug from get_reverse_complement (So I'll only count it once)
    #input: ATGCGAATGTAGCATCAAA, expected output: ['ATGCGAATG', 'ATGCTACATTCGCAT'] , actual output: ['ATGCGAATG']
	#input: ATGTGCATGAGATAGGATGGGATGCTTG, expected output: ['ATGTGCATGAGA', 'ATGCTTG', 'ATGGGATGCTTG', 'ATGCACAT'], actual output: ['ATGTGCATGAGA', 'ATGCTT', 'ATGGGATGCTTG']

    half_codons = [] #sets empty list for strand 1
    half_codons2 = [] #sets empty list for strand 2 (reverse of strand 1)
    all_the_codons = [] #sets empty list for strand 1 + strand 2
    half_codons += find_all_ORFs(dna) #finds all codons in strand 1
    half_codons2 += find_all_ORFs(get_reverse_complement(dna)) #finds all codons in strand 2
#    print 'hc2', half_codons2
    all_the_codons = half_codons + half_codons2 #creates of list of all the codons in strands 1 and 2
    return all_the_codons

def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """
    print 'input ATGCCCTAAATACGAATAACC, output[ATGCCC, ATGCTTATT]' + find_all_ORFs_both_strands('ATGCCCTAAATACGAATAACC')
    # YOUR IMPLEMENTATION HERE

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""

    #Also bugged as a result of the get_reverse_complement bug

    all_the_codons = find_all_ORFs_both_strands(dna) #sets all_the_codons equal to the list of codons from both strings
    if not all_the_codons: return '' #if no ATG is found return an empty string
    longest = all_the_codons[0] #sets longest codon as zero in length
    for i in range(1,len(all_the_codons)):
        if len(all_the_codons[i])>len(longest):
            longest = all_the_codons[i] #updates longest if new strand is longer than previous longest
    return longest

def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """

    print'input ATGAAATAACCCATGCCCGGGTAACCCGGGATGCCCGGGCCCTAA, output ATGCCCGGGCCC'+ longest_ORF('ATGAAATAACCCATGCCCGGGTAACCCGGGATGCCCGGGCCCTAA')

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """

    import random
    output = 0
    all_codons = list(dna) #turns dna into a list
    for i in range(num_trials):
        random.shuffle(all_codons) #shuffle the dna
        shuffled_dna = collapse(all_codons) #collapses lists into a single list
        longest = longest_ORF(shuffled_dna) #gets longest of shuffled DNA
        if len(longest)> output:
            output = len(longest) #updates longest if new shuffle DNA longest is longer than the previous longest value
    return output

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    final_aa_list = [] #sets empty list for amino acids
    list_of_all_aa = find_all_ORFs_both_strands(dna) #takes all the codons and puts them in a list
    for i in range(len(list_of_all_aa)):
        if len(list_of_all_aa[i])>=threshold: #if the sequence is longer than a threshold it will be added to the list
            strand = list_of_all_aa[i]
            aa = coding_strand_to_AA(strand) #the list is converted in a string
            final_aa_list.append(aa) #the string is added to the list final_aa_list
    return final_aa_list
    
        
#print longest_ORF_noncoding(dna,1500) #I did 1500 trials to find the longest noncoding strand to use as my threshold
#I got 684 and then 732
#print gene_finder(dna,684) #outputs amino acid sequence of genes
