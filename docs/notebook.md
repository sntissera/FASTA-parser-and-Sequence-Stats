# FASTA Parser and Sequence Statistics

## A beginner friendly project that parse FASTA files and provide sequence statistics.

### Overview

This simple project focuses on parsing compressed FASTA files can be downloaded via a link from any database and it provides simple statistical data of the sequences such as,

* Number of sequences
* GC content
* Sequence length distributions (total sequence length, average sequence length)
* K-mer frequencies

The program was tested for multiple FASTA files downloaded from the ncbi nucleotide and amino acid sequence database. Below are some of te files that were used to test the code.

1. The FASTA files contain DNA sequences extacted from stool and saliva samples of 9 patients (diseased) and 10 healthy subjects. The sequences were sequenced using v3-v4 16s rRNA sequencing to characterise the differences in microbiota between specimens of breast cancer and healthy surrounding tissue in adult Algerian females (Link to the relavant paper: https://doi.org/10.3390/genes16070806).

- Date and time of download: 10/09/2025, 11:48
- Source:  https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE243440 
- Download link: https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE243440&format=file&file=GSE243440%5Fdna%2Dsequences%2Efasta%2Egz

### Installation

The repository was first set up on the local device. It was later cloned to the designated GitHub repository implementing the following bash script on the terminal.

```bash
cd /path/of/the/project     # Change directory to the path where the project is stored.  
git init                    # Initialise Git
git add .                   # Add all files to staging
git commit -m "Initial commit" #Commit changes
git remote add origin https://github.com/username/repo-name.git    # Add the GitHub repo
git branch -M main          # make sure the local branch is main
git push -u origin main     # push the local directory to GitHub
```

To update the repository

```bash
cd /path/of/the/project     # Change directory to the path where the project is stored.  
git init                    # Initialise Git
git add filename            # to add a specific file
git commit -m "Describe your changes here"  #Commit changes
git push origin main        # Push to Github
```

### Project structure
project/
├── data/                   # Raw and processed data/ fasta files
    ├── filename.fasta.gz            
├── scripts/                # python scripts
    ├── main.py
    ├── parser.py
    ├── stats.py
├── docs/
    ├── documentation.md    # Extended documentation
└── README.md               # Project overview

### Program Structure

The program is composed of three classes named Parser, Statistics and Frequencies. The class Parser is written in parser.py file and the classes Statistics and Frequencies are written in stat.py file respectively. The classes are implemented in the main.py file and provides a statistical summary of the intended FASTA file.

### 


