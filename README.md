# paired_end_sorter
## What is it about?
Sometimes, when you do genomic assembly, you don't have clean data, especially with paired-end reads coming from 
Illumina technology. This script is used to re-assemble pairs of reads, coming from 2 differents files, not sorted, and 
with uncomplete pairs trapped in it. (readX.1 without a readX.2, etc...)
At the end, you will have a file with entrelaced pairs of paired-end reads.

## Version
Version 1.1

Next update: multi-processing

Time to treat:
- 659,996 and 593,837 reads (1,253,833 reads): 1h 21min 40sec
- 689,685 and 710,417 reads (1,400,102 reads): 1h 32min 8sec
- 903,535 and 799,652 reads (1,730,187 reads): 2h 36min 46sec

## Installation
You will need biopython and docopt:

        sudo pip3 install biopython docopt

## Documentation
Usage:

        ./paired_end_sorter.py <reads1> <reads2> -o <output_file> [options]

Options:

        --format, -f=<string>   The files format [default: fasta]
        --help, -h              Display this screen.
        --output, -o=<file>     The name of the output file (erase if already exist)
        --version,-v            The script version

## Licence
Gnu-GPL

## Contribute
Please fork and propose pull requests as much as you want.

I will be happy to optimize my script and help as much as I can.
