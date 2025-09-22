import requests, os, gzip
import pandas as pd

class Parser:
    '''Parse the FASTA files'''

    def __init__ (self,url:str,file_name:str,download_path:str):
        self.url = url
        self.__file_name = file_name
        self.download_path = download_path

    def  download_gz (self):
        '''Downloads the gzip files given a link'''

        if not self.download_path:
            self.download_path = '.'

        file_path = os.path.join(self.download_path, self.__file_name)
        os.makedirs(self.download_path, exist_ok = True)

        if not os.path.exists(file_path):
            print(f'Downloading the file to {file_path}')
            try:
                file = requests.get(self.url)
                file.raise_for_status()
                with open(file_path, 'wb') as f:
                    f.write(file.content)
                print('Download completed successfully')
            except requests.RequestException as e:
                print(f'Error downloading file {e}')
            except IOError as e:
                print(f'Error saving file {e}')
        else:
                print(f'The file already exists at {file_path}')
        return self

    def download_fasta(self):
        ''' Downloads fasta files given a link'''

        file_path = os.path.join(self.download_path, self.__file_name)
        os.makedirs(self.download_path, exist_ok = True)

        try:
            print(f'Downloading the file to {file_path}')
            response = requests.get(self.url,stream =True)
            response.raise_for_status()

            with open(file_path,'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            print('Download completed successfully')
        except requests.exceptions.RequestException as e:
            print (f'Error downloading file {e}')
        return self
    
    def readFile (self) -> list:
        ''' Open and read the FASTA files'''

        file_path = os.path.join(self.download_path, self.__file_name)
        
        if file_path.endswith(".gz"):
            open_file, mode = gzip.open, 'rt'
        else:
            open_file, mode = open, 'r'

        headers, sequences, current_sequence = [], [], []
        
        try:
            with open_file(file_path,mode) as f:
                for line in f:
                    line = line.strip()
                    if line.startswith ('>'):
                        if current_sequence:
                            sequences.append(''.join(current_sequence))
                        headers.append(line[1:])
                        current_sequence = []
                    else:
                        current_sequence.append(line)
                if current_sequence:
                    sequences.append(''.join(current_sequence))
            return headers, sequences
        
        except Exception as e: 
            print(f'Error reading file {e}')
            return [],[]

    def fasta_process (self) -> pd.DataFrame:
        ''' Converts the content in the fasta file to a dataframe'''
    
        headers, sequences = self.readFile()
        if not headers or not sequences:
            return pd.DataFrame()
        return pd.DataFrame({'Header': headers,
                            'Sequence': sequences})


