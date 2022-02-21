# This will be the main file
import urllib.request
import os.path

# Checks to see if the file exists, if it does NOT exist, download it and countine running.
if not(os.path.isfile('awslog.txt')):  
    print('You do not have the file, beginning file download with urllib2...')
    url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    urllib.request.urlretrieve(url, 'awslog.txt')
    print('File downloaded, resuming program.')
    
# Opens and splits file
file = open("awslog.txt","r")
read_file = file.read()
log = read_file.split('\n')

# Splits file into 12 seperate monthly files
# OCTOBER 1994
oct_94 = open("October_1994", "w")
for line in log:
    if "Oct/1994" in line:
        oct_94.write(line + "\n")
        
oct_94.close()

# NOVEMBER 1994
nov_94 = open("November_1994", "w")
for line in log:
    if "Nov/1994" in line:
        nov_94.write(line + "\n")
        
nov_94.close()

# DECEMBER 1994
dec_94 = open("December_1994", "w")
for line in log:
    if "Dec/1994" in line:
        dec_94.write(line + "\n")
        
dec_94.close()

# JANUARY 1995
jan_95 = open("January_1995", "w")
for line in log:
    if "Jan/1995" in line:
        jan_95.write(line + "\n")
        
jan_95.close()

# FEBRUARY 1995
feb_95 = open("February_1995", "w")
for line in log:
    if "Feb/1995" in line:
        feb_95.write(line + "\n")
        
feb_95.close()

# MARCH 1995
mar_95 = open("March_1995", "w")
for line in log:
    if "Mar/1995" in line:
        mar_95.write(line + "\n")
        
mar_95.close()

# APRIL 1995
apr_95 = open("April_1995", "w")
for line in log:
    if "Apr/1995" in line:
        apr_95.write(line + "\n")
        
apr_95.close()

# MAY 1995
may_95 = open("May_1995", "w")
for line in log:
    if "May/1995" in line:
        may_95.write(line + "\n")
        
may_95.close()

# JUNE 1995
jun_95 = open("June_1995", "w")
for line in log:
    if "Jun/1995" in line:
        jun_95.write(line + "\n")
        
jun_95.close()

# JULY 1995
jul_95 = open("July_1995", "w")
for line in log:
    if "Jul/1995" in line:
        jul_95.write(line + "\n")
        
jul_95.close()

# AUGUST 1995
aug_95 = open("August_1995", "w")
for line in log:
    if "Aug/1995" in line:
        aug_95.write(line + "\n")
        
aug_95.close()

# SEPTEMBER 1995
sep_95 = open("September_1995", "w")
for line in log:
    if "Sep/1995" in line:
        sep_95.write(line + "\n")
        
sep_95.close()

# OCTOBER 1995
oct_95 = open("October_1995", "w")
for line in log:
    if "Oct/1995" in line:
        oct_95.write(line + "\n")
        
oct_95.close()
    

