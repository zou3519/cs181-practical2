import os, sys, tarfile

''' python extract-data.py TAR_NAME
        Extract everything from TAR_NAME with the name before the .xml.
        asedl.Thing.xml -> Thing/asedl.Thing.xml
'''

def parse_name(s):
    stuff = s.split('.')
    return stuff[len(stuff)-2]

if len(sys.argv) != 2:
    print "Usage: python extract-data.py TAR_NAME"
    exit(0)

tar = tarfile.open(sys.argv[1] + '.tar.gz', 'r:gz')
for item in tar:
    directory = parse_name(item.name)
    tar.extract(item,path=(directory + "/"))
print 'Done.'