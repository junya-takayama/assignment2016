# -*- coding:utf-8 -*-
import CaboCha

c = CaboCha.Parser("-n1")
sent = "豊工に行っています。"
tree = c.parse(sent)
for i in range(tree.token_size()):
    token = tree.token(i)
    if token.ne is not "O":
        print(token.surface,token.ne)
