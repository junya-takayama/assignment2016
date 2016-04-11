import sys

#ファイルの読み込み
arg = sys.argv
f1 = open(arg[1],'r')

#単語ごとに改行
words = []
for line in f1:
    for word in line.strip().split():
        words.append(word)

#昇順ソート
s_words = sorted(words)

#辞書に登録
dict = {s_words[0]:1}
i = 1
while i < len(s_words):
    #登録済みならvalueを増加
    if s_words[i] == s_words[i-1]:
        dict[s_words[i]] += 1
    #未登録なら新規登録
    else:
        dict.update({s_words[i]:1})
    i += 1

#valueで降順ソート。重複していたらkeyでソート
s_freq = sorted(dict.items(), key = lambda x:(x[1],x[0]), reverse = True)

#上から10行文だけ出力
for k in range(0,10):
    print ("    ",s_freq[k][1],s_freq[k][0])
f1.close()
