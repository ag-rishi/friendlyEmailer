import ezgmail
import os

my_file = open("location of your text file of emails goes here", "r")
weblist = my_file.readlines()
weblist = list(map(lambda s: s.strip(), weblist))

os.chdir(r'C:\Python')
ezgmail.init()

i = 0
while i < len(weblist):
    try:
        ezgmail.send(weblist[i],"Your email body goes here. Use \n for a new line.")
    except:
        pass
    i = i + 1