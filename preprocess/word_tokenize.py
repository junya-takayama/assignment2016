import sys
from nltk.tokenize import word_tokenize, sent_tokenize

argv = sys.argv

text = open(argv[1]).read()
sent_tokenized = sent_tokenize(text)

word_tokenized = []
for sent in sent_tokenized:
    word_tokenized.extend(word_tokenize(sent))

print(word_tokenized)
