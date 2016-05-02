import sys
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import SennaChunkTagger

Ctagger = SennaChunkTagger('/usr/share/senna-v2.0')

#読み込んだテキストを文分割
sent_tokenized = sent_tokenize(open(sys.argv[1]).read())

#第1文だけ単語分割
word_tokenized = word_tokenize(sent_tokenized[0])

nlFlg = False #改行フラグ
for word, tag in Ctagger.tag(word_tokenized):
    if "B-" in tag:
        if nlFlg == True:
            print()
        else:
            nlFlg = True

        #句の種類と句の先頭の単語を表示
        print(str(tag).lstrip("B-"),"\11",str(word),end=" ")

    elif "I-" in tag:
        print(str(word),end=" ")
        nlFlg = True
