#this will be the main file
import urllib.request
import os.path
#checks to see if the file exists, if it does NOT exist, download it and countine running.
if not(os.path.isfile('awslog.txt')):  
    print('You do not have the file, beginning file download with urllib2...')
    url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    urllib.request.urlretrieve(url, 'awslog.txt')
    print('File downloaded, resuming program.')
    
# Opening a file
file = open("awslog.txt","r")

# Splits file by line into a list
read_file = file.read()
split_file = read_file.split('\n')
