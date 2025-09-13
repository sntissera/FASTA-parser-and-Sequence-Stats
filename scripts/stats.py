import pandas as pd 
from collections import Counter

class Statistics:
    ''' Calculate and analyse the relevant sequence statistics'''

    def __init__ (self,df):
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
    
    def compPercent (self):
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

    def freq(self):
        '''Calculates the k-mer frequencies given k'''
        pass

data = {
"header": [">seq1", ">seq2"],
"sequence": ["ATGCGTAC", "MKWVTFISLLFLFSSAYSR"]
}
df = pd.DataFrame(data)
seq = Statistics(df)
print(seq.gcContent())
