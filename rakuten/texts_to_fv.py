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
    for sent in jp_sent_tokenizer.tokenize(line.strip()):
        node = mecab.parseToNode(sent)
        node = node.next
        while node.next:
            
            if node.surface in count:
                count[node.surface] += 1
            else:
                count[node.surface] = 1
                index[node.surface] = len(count)
            print(str(index[node.surface])+":"+str(count[node.surface]),end=' ')
            node = node.next
    print()
