# -*- coding:utf-8 -*-
import CaboCha

c = CaboCha.Parser()

sent = "豊工に行っています。"
tree = c.parse(sent)
print(tree)
print(tree.toString(CaboCha.FORMAT_TREE))
