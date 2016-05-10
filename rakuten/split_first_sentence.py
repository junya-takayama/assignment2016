import sys
from nltk.tokenize import RegexpTokenizer
import gzip

jp_sent_tokenizer = RegexpTokenizer(u'[^！？。]*[！？。]?')

f_line = gzip.open(sys.argv[1],"rt").readlines()[0]

print(jp_sent_tokenizer.tokenize(f_line))
