# -*- coding:utf-8 -*-
import MeCab

mecab = MeCab.Tagger('-Ochasen')
mecab.parse("") #おまじない
sent = "豊工に行っています。"
node = mecab.parseToNode(sent)
node = node.next
while node.next:
    surface = node.surface
    elem = node.feature.split(",")
    print(surface,end='')
    
    print("\t", elem[0], "  ",elem[6])
    node = node.next
