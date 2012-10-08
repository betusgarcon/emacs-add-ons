#!/usr/bin/python
'''this is my first entire python programme'''

import os
ls = os.linesep
os.li
# get the input
print "please input the new file name..."
fname = input('>')

while True:
    if os.path.exists(fname):
        print "ERROR:'%s' is exists!,please input again!" % fname
        break
    else:
        break

# get file content and put them into the memory
all = []

print "\n Enter lines ('.' by itself to quit)\n"

while True:
    line = input('>')
    if line == '.':
        break
    else:
        all.append(line)

# output the file to the console
fobj = open(fname,'w')
fobj.writelines(['%s%s' % (x,ls) for x in all])
fobj.close()

# print 'what is ls?'ls
print 'all over now!! \n author:Betus'

