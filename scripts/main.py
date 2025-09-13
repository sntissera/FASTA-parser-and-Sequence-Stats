from parser import Parser
from stats import Statistics, Frequencies
import pandas as pd

#Inputs given by the user
url = input('Enter the link: ')
file_name = input('Enter the name of the file to be renamed as: ')
download_path = input ('Enter the download path (press enter for current directory): ')

#Downloading the files
file = Parser(url,file_name,download_path)
file.download()

#Analysing the sequences
df = file.unzip()

raw_data1 = Statistics(df)
processed = pd.DataFrame(df.iloc[:,0])

#Calculate the length of each sequence
processed['Length'] = raw_data1.lenSeq()

#Calculate the composition and its percentage for each sequence
processed['Composition'] = raw_data1.composition()
processed['Percentage composition'] = raw_data1.compPercent()

#Calculate the GC content
processed['GC content'] = raw_data1.gcContent()

#Summary
print(processed)

#Calculate the k-mer frequencies
k = int(input('Enter the k value: '))
raw_data2 = Frequencies(df,k)
new = pd.DataFrame(df.iloc[:,0])
new['K-mer frequencies'] = raw_data2.countSubset()
print(new)






