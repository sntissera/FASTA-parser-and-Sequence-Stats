import pandas as pd 
from collections import Counter

class Statistics:
    ''' Calculate and analyse the relevant sequence statistics'''

    def __init__ (self,df:pd.DataFrame):
        self.df = df
        
    def lenSeq (self) -> list:
        ''' Returns the length of the sequence'''
        
        results = []
        for s in self.df.iloc[:,1]:
            results.append(str(len(s)) + ' bp')
        return results
    
    def composition(self) -> list:
        '''Calculates the composition of the sequence'''
        
        results = []
        for seq in self.df.iloc[:,1]:
            counts = Counter(seq)
            formatted = {k: counts[k] for k in sorted(counts)}
            results.append(formatted)
        return results
    
    def compPercent (self) -> list:
        '''Calculates the percentage of the composition of a sequence'''

        results = []
        for comp in self.composition():
            counts = Counter(comp)
            total = sum(counts.values())
            formatted = {k: (round((v/total)*100,2)) for k,v in counts.items()}
            results.append(formatted)
        return results
    
    def gcContent(self) -> list:
        '''Calculates the GC content of DNA/RNA sequences'''

        results = []
        for comp in self.compPercent():
            bases = set(comp.keys())
            dna = {'A','T','G','C'}
            rna = {'A','U','G','C'}

            if bases.issubset(dna) or bases.issubset(rna):
                gc_percent = comp.get('G') + comp.get('C')
                results.append(f'{gc_percent:.2f}%')
            else:
                results.append(None)
            
        return results

class Frequencies:
    '''Calculates the k-mer frequencies when k is given'''

    def __init__ (self,df:pd.DataFrame, k:int):
        self.df = df
        self.k = k
            
    def subSet (self) -> list:
        '''Returns a list of k-mers'''
            
        results = []
        for seq in self.df.iloc[:,1]:
            k_mers = []
            for i in range(len(seq) - self.k + 1):
                k_mers.append(seq[i:self.k + i])
            results.append(k_mers)
        return results
    
    def countSubset (self) -> list:
        ''' Returns the number of k-mers per sequence'''
        
        results = []
        for s in self.subSet():
            counts = dict(Counter(s))
            results.append(counts)
        return results

