import sys
from nltk.tokenize import word_tokenize, sent_tokenize

argv = sys.argv

sent_tokenized = sent_tokenize(open(argv[1]).read())
word_tokenized = []

for sent in sent_tokenized:
    word_tokenized.extend(word_tokenize(sent))

dict = {}
for word in word_tokenized:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1

s_dict = sorted(dict.items(), key = lambda x:(x[1],x[0]), reverse = True)

for k in range(0,10):
    print("\11",s_dict[k][1],s_dict[k][0])

