from parser import Parser
from stats import Statistics, Frequencies
import pandas as pd

def add_data(df,column_name,results):
    '''Add data to the dataframe'''

    df[column_name] = results
    return df
    
#Inputs given by the user
url = input('Enter the link: ')
file_name = input('Enter the name of the file to be renamed as: ')
download_path = input ('Enter the download path (press enter for current directory): ')

#Downloading the files
file = Parser(url,file_name,download_path)
file.download()

#Analysing the sequences
df = file.unzip()

seq = Statistics(df)
lengths = seq.lenSeq()
comp = seq.composition()
comp_percent = seq.compPercent()
gc = seq.gcContent()

seq1 = Frequencies(df,3)
sbset = seq1.countSubset()

df = (add_data(df,'Length',lengths))
df = (add_data(df,'Composition',comp))
df = (add_data(df,'Percentage',comp_percent))
print(add_data(df,'K-mer Freq',sbset))






