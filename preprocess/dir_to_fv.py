import sys
import shelve
import os
from nltk.tokenize import word_tokenize, sent_tokenize

for aFile in os.listdir(sys.argv[1]):
    count = {}
    index = shelve.open('database/'+'doc_to_fv_'+str(aFile).replace(".txt","")+'.db')
    for sent in sent_tokenize(open(sys.argv[1] +'/'+ aFile).read()):
        for word in word_tokenize(sent):
            if word in count:
                count[word] +=1
            else:
                count[word] = 1
                index[word] = len(count)
                
    for key, num in sorted(index.items(), key = lambda x:x[1]):
        print(str(num)+":"+str(count[key]),end=' ')
    print()
    index.close()

