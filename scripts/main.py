import requests, os, gzip

#Downloading the FASTA files
url = input('Enter the link: ')
file_name = input('Enter the name of the file: ')
download_path = input ('Enter the download path (press enter for current directory): ')

if not download_path:
    download_path = '.'

file_path = os.path.join(download_path, file_name)
os.makedirs(download_path, exist_ok = True)

if not os.path.exists(file_path):
    print(f'Downloading the file to {file_path}')
    try:
        file = requests.get(url)
        file.raise_for_status()
        with open(file_path, 'wb') as f:
            f.write(file.content)
        print('Downlaod completed successfully')
    except requests.RequestException as e:
        print(f'Error downloading file {e}')
    except IOError as e:
        print(f'Error saving file {e}')
else:
    print(f'The file already exists at {file_path}')

#parsing the file
open_file = gzip.open if file_name.endswith('.gz') else open

with open_file(file_name,'r') as f:
    for i in range(10):
        line = f.readline()
        if not line:
            break
        print(line.strip())