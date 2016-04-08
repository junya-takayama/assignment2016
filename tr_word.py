import sys

arg = sys.argv
f1 = open(arg[1],'r')


for line in f1:
    for word in line.strip('\n').split():
        print (word)
f1.close()
