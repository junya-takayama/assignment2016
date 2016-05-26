"""
クラスを利用してみた
"""
import sys
import xml.etree.ElementTree as et
import re
from collections import OrderedDict

class SyntacticCategory:
    def __init__(self,dic):
        for key in dic:
            self.__dict__[key] = dic[key]

class Sentence:
    def __init__(self,sent_id,roots,dic_ccg):
        self.id = sent_id
        self.roots = roots.split(' ')
        self.ccg = dic_ccg

def reCcg(cat):
    """
    カテゴリから余分な情報を削除しておく
    """
    cat = re.sub(u'\[.*?\]','',cat)
    cat = cat.replace('\\','＼')
    return cat

def getInfo():
    """
    各<span>とそれに対応する<token>の属性をまとめてインスタンス化
    インスタンス変数の名前は属性の名前と同一
    @dic_sent : {文のID:対応するインスタンス}
    @dic_ccg  : {統語範疇のID:対応するインスタンス}
    """
    dic_sent = OrderedDict()
    dic_ccg = OrderedDict()
    for sent in tree.iter('sentence'):
        nList = []
        s_id = sent.attrib.get('id')
        roots = sent.find(".//ccg").attrib.get('root')
        for node in sent.iter('span'):
            n = node.attrib
            n['category'] = reCcg(n.get('category'))
            if 'terminal' in n:
                t_id = n.get('terminal')
                t_attrib = root.find(".//*[@id='"+t_id+"']").attrib
                del t_attrib['id'] # id属性はCCG側と重複するので削除
                n.update(t_attrib)
            nList.append(n.get('id'))
            dic_ccg[n.get('id')] = SyntacticCategory(n)
        dic_sent[s_id] = Sentence(s_id,roots,nList)
    return dic_sent,dic_ccg

def printCcgTree(span_id,c):
    """
    CCGツリーを表示。
    @span_idで指定されたIDを持つノードに対し、
    @cで与えられた階層分だけインデントしてカテゴリと表層を表示する。
    そのノードが持つ、子ノードのIDと、一つ深くした階層を引数に再帰的に同関数を呼び出す。
    """
    node = ccg[span_id]
    line = re.sub(u's.*?_','',span_id).ljust(5)
    for i in range(0,c):
        line += '     '
    line += ('[\''+node.category+'\']').ljust(15)
    if hasattr(node,'surf'):
        line += node.surf
    print(line)
    if hasattr(node,'child'):
        c += 1
        for c_id in node.child.split(' '):
            printCcgTree(c_id,c)
    else:
        return 0

def sentence(sent_id):
    sentence = root.find(".//*[@id='"+sent_id+"']").text.strip()
    return sentence

def findTerm():
    print()

if __name__ == "__main__":
    with open(sys.argv[1],'rt') as f:
        tree = et.parse(f)
    root = tree.getroot()
    sent,ccg = getInfo()

    for sent_id in sent.keys():
        print('sentence id : '+sent_id)
        print("sentence    : "+sentence(sent_id))
        for root_id in sent[sent_id].roots:
            printCcgTree(root_id,0)
