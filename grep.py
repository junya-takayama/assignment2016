import sys

list = sys.argv
f1 = open(list[1],'r')

for line in f1:
    if line.find(list[2]) >= 0:
        print (line)

f1.close()
