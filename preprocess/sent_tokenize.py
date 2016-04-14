import sys
from nltk.tokenize import sent_tokenize

argv = sys.argv

text = open(argv[1]).read()
sent_tokenized = sent_tokenize(text)

print(sent_tokenized)
