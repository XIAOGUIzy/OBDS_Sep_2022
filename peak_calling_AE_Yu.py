#Code to find overlapping intervals comparing one bedfile to another
import argparse
import sys

parser = argparse.ArgumentParser() # Create a parserparser.add_argument('-o', # Name of option 
parser.add_argument('-a', # Name of option          
                "--input1",
                dest='bed_a', # Variable name to store option
                help='input file1 in bed format'
                ) # Help text (optional)
parser.add_argument('-b', # Name of option          
                "--input2",
                dest='bed_b', # Variable name to store option
                help='input file2 in bed format'
                ) # Help text (optional)
parser.add_argument('-o', # Name of option 
                "--output",
                dest='output', # Variable name to store option
                help='merged intervals of 2 input bed files', # Help text (optional
                )
# parser.add_argument('-st', # Name of option 
#                 "--stdout",
#                 dest='standout', # Variable name to store option
#                 help='output file as standard output', # Help text (optional
#                 action="store_true",
#                 default= False)
args = parser.parse_args()


#! /c/Users/ayesh/Documents/Ayesha/Medical/Oxford Registrar/WIMM DPhil Zeta globin/repositories_github/OBDS_Sep_2022/Day5_python

with open (args.bed_a, mode="r") as bed_a: #input first bedfile
    with open (args.bed_b, mode="r") as bed_b: #input second bedfile
        with open (args.output, mode="w") as output: # set the output file to save overlap info
            for index_a, line_a in enumerate(bed_a): # to set file a as comparison file
                list_bed_a = line_a.split("\t") #line bed a is a list now
                bed_b.seek(0) # start comparing from the first line of file b and loop round file b til all file a compared
                for index_b, line_b in enumerate(bed_b):
                    list_bed_b = line_b.split("\t") #line bed b is a list now
                    a_chrname = list_bed_a[0]
                    a_chrstart = int(list_bed_a[1])
                    a_chrstop = int(list_bed_a[2])
                    b_chrname = list_bed_b[0]
                    b_chrstart = int(list_bed_b[1])
                    b_chrstop = int(list_bed_b[2])
                    # output_int = []
                    if a_chrname == b_chrname:
                        if (a_chrstart >= b_chrstart and a_chrstart <= b_chrstop) or (b_chrstart >= a_chrstart and b_chrstart <= a_chrstop):
                            output.write("\t".join([str(a_chrname), str(a_chrstart), str(a_chrstop)]) + "\n")

#counting lines in the output file i.e. number of overlapping intervals
file = open("output", "r")
line_count = 0
for line in file:
        if line != "\n":
            line_count += 1
file.close()

print(line_count)