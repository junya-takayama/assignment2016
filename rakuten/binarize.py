import sys

nLabel = ''
for oLabel in open(sys.argv[1],"r"):
    nLabel += '1\n' if int(oLabel) >=4 else '-1\n' 
    
open(sys.argv[2],"w").write(nLabel) 
