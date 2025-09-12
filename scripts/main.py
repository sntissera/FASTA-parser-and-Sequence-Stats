from parser import Parser

url = input('Enter the link: ')
file_name = input('Enter the name of the file to be renamed as: ')
download_path = input ('Enter the download path (press enter for current directory): ')

file = Parser(url,file_name,download_path)
file.download()
file.unzip()
file.



