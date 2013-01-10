## File Dupe Nuker
##(because dupes suck)

import os, re


print "Dylan's Dupe Nuker Version 1.0"


Dupe_Directory = '/Users/Pierce/Music/'
Files_List = {}
Kill_Count = 0

## Recursively look for more directories

for dirname, dirnames, filenames in os.walk(Dupe_Directory):
    for subdirname in dirnames:
        print os.path.join(dirname,subdirname)
    for filename in filenames:
        print os.path.join(dirname,filename)
        
## Append all non-directory files to a dictionary
        ## Files_List {key:value} = {filename: file's location}
        
        Files_List[filename[:-4]] = os.path.join(dirname,filename)

## Look for duplicates, if found delete them
for File in Files_List:
    Dupe_Suffixes = [" 2", " 3"," 4"," 5"," 6"," 7"," 8"," 9"," 10"]
    for Suffix in Dupe_Suffixes:
        Dupe = File + Suffix
        print 'Looking for ' + Dupe
        if Dupe in Files_List:
            print 'I found a dupe called: ' + Dupe
            os.remove(Files_List[File + Suffix])
            print '...deleted'
            Kill_Count = Kill_Count + 1
        else:
            print 'nope'
    
print "Complete!"
print str(Kill_Count) + " songs deleted"
