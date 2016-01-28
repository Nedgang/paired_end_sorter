# paired_end_sorter
## What is it about?
Sometimes, when you do genomic assembly, you don't have clean data, especially with paired-end reads coming from 
Illumina technology. This script is used to re-assemble pairs of reads, coming from 2 differents files, not sorted, and 
with uncomplete pairs trapped in it. (readX.1 without a readX.2, etc...)
At the end, you will have a file with entrelaced pairs on paired-end reads.

## Version
Version 1.0

Time to treat 2 files with 659,996 and 593,837 reads: 1h 21min 40sec

## Installation
You will need biopython:

        sudo pip3 install biopython

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
