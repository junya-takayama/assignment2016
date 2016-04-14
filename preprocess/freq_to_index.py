import sys
from nltk.tokenize import word_tokenize, sent_tokenize

argv = sys.argv

#sent_tokenized = sent_tokenize(open(argv[1]).read())
#word_tokenized = []

count = {}
index = {}
for sent in sent_tokenize(open(argv[1]).read()):
    for word in word_tokenize(sent):
        if word in count:
            count[word] +=1
        else:
            count[word] = 1
            index[word] = len(count)

print("\11 Order\11 freq\11 key")
for key, num in sorted(index.items(), key = lambda x:x[1]):
    print("\11",num,"\11",count[key],"\11",key)
    if num == 10:
        break
