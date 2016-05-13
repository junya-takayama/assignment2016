import sys
from nltk.tokenize import RegexpTokenizer
import gzip
import MeCab

jp_sent_tokenizer = RegexpTokenizer(u'[^！？。]*[！？。]?')
mecab = MeCab.Tagger('-Ochasen')
mecab.parse("")
f_line = gzip.open(sys.argv[1],"rt").readlines()
count = {}
index = {}

for line in f_line:
    count = {}
    for sent in jp_sent_tokenizer.tokenize(line.strip()):
        node = mecab.parseToNode(sent)
        node = node.next
        while node.next:
            if node.surface in count:
                count[node.surface] += 1
            else:
                count[node.surface] = 1
                if not node.surface in index:
                    index[node.surface] = len(index)+1
            node = node.next
    vector= []
    for key, num in sorted(count.items(), key = lambda x:x[1]):
        vector.append([index[key],num])
    vector.sort()
    for i ,c in vector:
        print(str(i)+":"+str(c),end=' ')
    print()
