import MeCab
mecab = MeCab.Tagger('mecabrc')

sent = '豊工に行っています。'

print(mecab.parse(sent))
