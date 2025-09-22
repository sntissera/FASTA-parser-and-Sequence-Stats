# FASTA Parser and Sequence Statistics

## A beginner friendly project that parse FASTA files and provide sequence statistics.

### Overview

This simple project focuses on parsing compressed FASTA files can be downloaded via a link from any database and it provides simple statistical data of the sequences such as,

* Number of sequences
* GC content
* Sequence length distributions (total sequence length, average sequence length)
* K-mer frequencies

The program was tested for multiple FASTA files downloaded from the ncbi nucleotide and amino acid sequence database. Below are some of the files that were used to test the code.

1. v3-v4 16s rRNA sequencing of breast cancer and healthy surrounding tissue in adult Algerian females: https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE243440&format=file&file=GSE243440%5Fdna%2Dsequences%2Efasta%2Egz

### Project structure
project/
├── data/                   # Compressed/ uncompressed FASTA files
    ├── filename.fasta.gz
    ├── filename.fasta            
├── scripts/                # python scripts
    ├── main.py
    ├── parser.py
    ├── stats.py
├── docs/
    ├── documentation.md    # Extended documentation
└── README.md               # Project overview

### Installation
Download the python scripts from `scripts/`. Make sure to save them under the same directory. Once setup, open `main.py` file and run the code.

### Program Structure

The program is composed of three classes named Parser, Statistics and Frequencies. The class Parser is written in parser.py file and the classes Statistics and Frequencies are written in stat.py file respectively. The classes are implemented in the main.py file and provides a statistical summary of the intended FASTA file.

### 


