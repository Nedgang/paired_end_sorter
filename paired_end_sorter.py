#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Take files with reads 1 and reads 2, find the paired sequences, and return a
file containing entrelacing paired-end reads.
/!\
Be careful, it's design to work on pairs named like that: BigIdentifier_read1
If your reads have not this kind of naming, change it or alter the code, as
you want.

Usage:
    ./data_cleaner.py <reads1> <reads2> (--output=<file>) [options]

Options:
    --format, -f=<string>   The files format [default: fasta]
    --help, -h              Display this screen.
    --output, -o=<file>     The name of the output file (erase if already exist)
    --version,-v            The script version

"""

##########
# IMPORT #
##########
import os

from docopt import docopt
from Bio import SeqIO

#############
# ARGUMENTS #
#############
if __name__ == "__main__":
    args = docopt(__doc__, version="1.0")

########
# MAIN #
########
def main(args):
    """
    Just a regular main, which call all the differents functions, and do 
    barely nothing else (matters).
    """
    # First of all, extract the sequences, and sort them by their ID.
    list_reads1 = sorted(_extract(args["<reads1>"], args["--format"]),
                    key=lambda seq: seq.id)
    list_reads2 = sorted(_extract(args["<reads2>"], args["--format"]),
                    key=lambda seq: seq.id)
    # Read the smallest file, maybe not usefull, i've to make test.
    if len(list_reads1) < len(list_reads2):
        pair_find = _find_paires(list_reads1, list_reads2)
    else: 
        pair_find = _find_paires(list_reads2, list_reads1)
    # Print result in a file.
    print_file(pair_find, args["--format"], args["--output"])


#############
# FUNCTIONS #
#############
def _extract(path_file, file_format):
    """
    Extract all infos from the sequences file.
    """
    # A generator, juste because it's beautifull
    label_list = [sequence for sequence in
                  SeqIO.parse(os.path.abspath(path_file), file_format)]
    return label_list

def _find_paires(list_reads1, list_reads2):
    """
    Read each sorted list, find sequences with similar ID and return a list
    containing each pair interlaced (1.1, 1.2, 2.1, 2.2, 3.1, etc).
    """
    return_list = []
    for read1 in list_reads1:
        for read2 in list_reads2:
            if read1.id[:-3] == read2.id[:-3]:
                return_list.append(read1)
                return_list.append(read2)
                list_reads2 = list_reads2[list_reads2.index(read2)+1:]
                break 
            elif read1.id[:-3] < read2.id[:-3]:
                list_reads2 = list_reads2[list_reads2.index(read2):]
                break
    return return_list

def print_file(selected_seq, seq_type, output):
    """
    selected_seq: a list
    seq_type: string
    output: file path
    """
    output_file = open(output, "w")
    SeqIO.write(selected_seq, output_file, seq_type)
    output_file.close

##########
# LAUNCH #
##########
if __name__ == "__main__":
    main(args)
