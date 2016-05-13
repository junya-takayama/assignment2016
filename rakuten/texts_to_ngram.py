import sys
from nltk.tokenize import RegexpTokenizer
import gzip
import MeCab

jp_sent_tokenizer = RegexpTokenizer(u'[^！？。]*[！？。]?')
mecab = MeCab.Tagger('-Ochasen')
mecab.parse("")
f_line = gzip.open(sys.argv[1],"rt").readlines() #第一引数で読み込むtxt.gzファイルを指定
count = {}
index = {}
n = int(sys.argv[2]) #第二引数でn-gramのnを指定(n=1,2,3,･･･)
for line in f_line:
    count = {}
    for sent in jp_sent_tokenizer.tokenize(line.strip()):
        node = mecab.parseToNode(sent)
        node = node.next

        while node.next:
            #--------n-gram----------
            i = n
            word = ''
            node2 = node
            while node2 and i!=0:
                #n回分単語を追加していく
                word += node2.surface
                i = i - 1
                node2=node2.next
            #-------------------------
            
            #辞書に追加
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
                if not word in index:
                    index[word] = len(index)+1
            node = node.next
    
    #素性ベクトルの生成
    vector= []
    for key, num in sorted(count.items(), key = lambda x:x[1]):
        vector.append([index[key],num])
    vector.sort()

    #表示
    for i ,c in vector:
        print(str(i)+":"+str(c),end=' ')
    print()
