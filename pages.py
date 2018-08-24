import sys       
import subprocess
import re

# Calls the R system specifying that commands come from file commands.R
# The commands.R provided with this assignment will read the file named
# data and will output a histogram of that data to the file pageshist.pdf
def runR( ):
    res = subprocess.call(['R', '-f', 'commands.R'])

# log2hist analyzes a log file to calculate the total number of pages
# printed by each user during the period represented by this log file,
# and uses R to produce a pdf file pageshist.pdf showing a histogram
# of these totals.  logfilename is a string which is the name of the
# log file to analyze.
#

#def Find(pat, text):
#    match = re.search(pat, text)
#    if match:
#        print match.group()
#    else
#        print 'Not Found'

def log2hist(logfilename):
    # fill in your code here

    key_user = 'user:'
    key_pages = 'pages:'
    
    # initialize dictionary to store values
    logtable = {}

    # open file for reading
    with open(logfilename) as file:
        file_info = file.readlines()
       
    # make each line of file into a list
    for line in file_info:
        split_line = line.split()
       ## print split_line

        ## find the index of key_user and get the next element in the
        ## list to get the username
        if key_user in split_line:
            spot = split_line.index(key_user)
            username = split_line[spot + 1]
##            print username

            ## same thing with pages...
            place = split_line.index(key_pages)
            pages = int(split_line[place + 1])
##            print pages

            ## now add to the logtable...
            if username in logtable:
                logtable[username] += pages
            else:                
                logtable[username] = pages
            

##    for key,val in logtable.items():
##        print key, '->', val
##    print "Value : %s" % logtable.values()

    with open('data', 'w') as datafile:
        for numpages in logtable.values():
            datafile.write("%s" % numpages)
            datafile.write('\n')
    
    #runR()
    datafile = runR()

if __name__ == '__main__':
    log2hist(sys.argv[1])   # get the log file name from command line

# line above may be changed to log2hist("log") to make the file name
#    always be log

