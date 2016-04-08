import sys

file = sys.argv
f = open(file[1],'r')

for line in f:
    print (line),

f.close()
