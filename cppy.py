# coding: UTF-8
import glob
import sys
import os

def searchpy(drc,files):
    #@drcで指定したディレクトリ以下の.pyファイルを全て検索し、
    #そのパスが入ったリストを返す再帰関数
    #@files : [] (必ず空のリストを渡す)

    files.extend(glob.glob(drc +'*.py'))
    drcs = glob.glob(drc +'*/')
    if len(drcs) is not 0:
        for aDrc in drcs:
            searchpy(aDrc,files)
    return files

def copy(file,cpdir):
    #@file　で指定されたパスのファイルを、@cpdir　で指定されたパスのディレクトリに複製する

    dirpath = os.path.dirname(cpdir+file)
    choice = input(file+':コピーしますか？\'y\' or \'n\'==> ').lower()
    if choice in ['y','yes']:
        if os.path.exists(dirpath) is False:
            os.makedirs(dirpath)
        f = open(cpdir+file,'w')
        for line in open(file,'r'):
            f.write(line)
        f.close()
        message = 'コピー完了'
    else:
        message = 'コピー中止'
    return message

for file in searchpy(sys.argv[1],[]):
    print(copy(file,'../github/assignment2016/')+'\n')
