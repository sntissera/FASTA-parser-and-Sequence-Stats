import requests, os, gzip

class Parser:
    '''Parse the FASTA files'''

    def __init__ (self,url,file_name,download_path):
        self.__url = url
        self.__file_name = file_name
        self.download_path = download_path

    def  download (self):
        '''Downloads the FASTA files given a link'''

        if not self.download_path:
            self.download_path = '.'

        file_path = os.path.join(self.download_path, self.__file_name)
        os.makedirs(self.download_path, exist_ok = True)

        if not os.path.exists(file_path):
            print(f'Downloading the file to {file_path}')
            try:
                file = requests.get(self.__url)
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

    def unzip(self):
        ''' Unzip gzip files'''

        file_path = os.path.join(self.download_path if self.download_path else '.', self.__file_name)

        if file_path.endswith ('.gz'):
            open_file = gzip.open
            mode = 'rt'

        else:
            open_file = open
            mode = 'r'

        try:
            with open_file(file_path,mode) as f:
                for i in range(10):
                    line = f.readline()
                    if not line:
                        break
                    print(line.strip())
        except FileNotFoundError:
            print('File not found')
        except Exception as e:
            print('Error reading file')