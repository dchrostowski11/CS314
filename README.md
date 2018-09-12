Principles of Programming Languages


Project Description

CS 314, Spring 2018, Prof. Steinber

Project 3: Python

First download and install python if you do not already have in on your machine. You can download it from http://www.python.org/download/. Download version 2.7.14. If you already have python, type the command 
python - -version
(that is a space followed by two minus signs followed by version) to a command window to check the version you have. (Command windows are also known as Terminal windows or XTerms). Any version from 2.5 – 2.7.x should be ok. Please do NOT use version 3.x without first checking with Prof. Steinberg.

Documentation can be found at http://docs.python.org . Read the tutorial for version 2.7 and skim documentation on the modules subprocess and re. Or you can use the Google videos you were assigned in class (but that does not cover the subprocess module).

Next, download the attached file project3.zip, and unzip it to create a folder named project3.

Finally, download and install the R system.  http://www.r-project.org/ is the R home page, download from http://lib.stat.cmu.edu/R/CRAN/ . R is a system for analyzing and visualizing data. We will use a tiny fraction of its abilities: the ability to produce a histogram. We will use it as a black box; you should not need to learn anything about R to do this project.

*** If you are installing R under windows, be sure to add it to your “path”. I am not sure what version of Windows the following is for, but all versions should be similar:

Go to System Properties, Advanced, Environment Variables, find "path" under System Variables, and added
;C:\Program Files\R\R-3.0.2\bin
The 3.0.2 part needs to be replaced with whatever version number you install.
You may need to restart your computer after doing this to make it take effect.

This project is an example of using Python to tie together existing programs. In particular, we imagine that we have printing software which generates a log file each day, describing the printing jobs done that day. Each print job outputs a line in the log file giving the user name and pages printed for that job. You are to write a python program which reads a log file, figures out the total number of pages printed for each user, and calls on the R system to produce a pdf file containing a histogram of this data.

Details

Each print job on the printer causes a line like the following to appear in the log file:

180.186.109 code: k user: louis qux: abc xuz pages: 32 def

The significant parts of this are user: louis and pages: 32. You can assume that each print job produces a line that includes the string “user:<spaces><name><spaces>” followed (maybe after some other things) by the string “pages:<spaces><number><spaces-or-eol>” where <spaces> is one or more spaces, <spaces-or-eol> is one or more spaces or the end of the line, <name> is a string of digits and lower case letters, and <number> is a string of digits indicating how many pages the user printed for this print job. There may be other things between the name and the following “pages:”. There may be other lines in the file as well, but they will not include the string “user:”, (although they may contain “pages:”) and they should be ignored. Note that some of these other lines may be entirely blank. You may assume that “pages:” can only appear on a line after “user:”, not before it. You may not assume anything else about the format of lines in the log file.

The folder project3 includes 2 example log files: log and logsmall.

You are to write your program in the file pages.py, which you can find in the project3 folder. The file already has one finished function in it, runR. If you call runR( ) from python, it will start up R and cause R to read commands from the file commands.R. After it finishes these commands, R will exit and runR will return.

Pages.py also has the header for the function log2hist(logfilename). This function should read a log file, whose name is the value of logfilename. It should produce a file named data with one line for each user containing the total pages printed for that user. (The file data.example in folder project3 is an example showing the format that data should have, using the file logsmall as the input. The lines in the data can be in any order. Note that only total page counts show up in the data, not user names.) Finally, log2hist should call runR, which will cause R to produce the file pageshist.pdf with the histogram.

The line

log2hist(sys.argv[1])

calls log2hist with the logfile from the command line. E.g., if the command line that starts the program is

python pages.py logsmall

the program will use logsmall as the log file name. Alternatively, you may edit the log2hist(sys.argv[1]) to be log2hist(“log”) to always use the file named log.

Turn in your edited pages.py as an attachment to this assignment. See Sakai for the due date and time.


