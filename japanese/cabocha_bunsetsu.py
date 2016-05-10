# -*- coding:utf-8 -*-
import CaboCha

c = CaboCha.Parser()

sent = "豊工に行っています。"
tree = c.parse(sent).toString(CaboCha.FORMAT_TREE)

for line in tree.split():
    chunk = line.split("-")
    print(chunk[0])
