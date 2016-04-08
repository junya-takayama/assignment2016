import sys

file = sys.argv
f1 = open(file[1],'r')
f2 = open(file[2],'w')

for line in f1:
#   print (line),
    f2.write(line)

f1.close()
f2.close()
