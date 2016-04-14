import sys
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import SennaTagger

argv = sys.argv

sent_tokenized = sent_tokenize(open(argv[1]).read())
word_tokenized = word_tokenize(sent_tokenized[0])

tagger = SennaTagger('/usr/share/senna-v2.0')

for a,b in tagger.tag(word_tokenized):
    print(b,"\11",a)
