import sys
import shelve
import os
from nltk.tokenize import word_tokenize, sent_tokenize

try:
    index = shelve.open('database/doc_to_fv.db')
    if len(sys.argv) != 3:
        raise Exception("引数エラー")
    for aFile in os.listdir(sys.argv[1]):
        print(str(sys.argv[2]),end='')
        count = {}
        index = shelve.open('database/doc_to_fv.db')
        for sent in sent_tokenize(open(sys.argv[1] +'/'+ aFile).read()):
            for word in word_tokenize(sent):
                if word not in index:
                    index[word] = len(index) + 1
                    count[index[word]] =1
                else:
                    if index[word] in count:
                        count[index[word]] += 1
                    else:
                        count[index[word]] = 1

        for num, freq in sorted(count.items(),key = lambda x:x[0]):
            print(" "+str(num)+":"+str(freq),end='')
        print()
except Exception as e:
    print("Error Occured : ",e)

finally:
    index.close()

