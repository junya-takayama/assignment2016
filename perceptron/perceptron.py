import sys
import time
import random
import math
from optparse import OptionParser
"""
exec:1000  acc:82.5% time:02m04s
exec:5000  acc:82.5% time:9m58s
exec:10000 acc:      time:
"""

def read_instance(review):
    #2.8.1
    l_line = review.strip().split(' ')
    l_fv = []
    label= int(l_line[0])
    del l_line[0]
    append = l_fv.append
    sum_c = 0
    for fv in l_line:
        i,c = fv.split(":")
        i = int(i)
        c = int(c)
        sum_c += c*c
        append([i,c])
    norm = math.sqrt(sum_c) if(options.normalize==True) else 1
    l_fv_norm = [(index,count/norm) for index,count in l_fv]
    if(options.bias==True):
        append((0,1))
    return (label,l_fv_norm)

def read_data(data):
    #2.8.2
    v_max = 0
    l_instance = [read_instance(review) for review in open(data)]
    for i in range(len(l_instance)):
        tmp_max = max(l_instance[i][1],key=lambda x: x[0])[0]
        v_max = max(v_max,tmp_max)    
    return l_instance,v_max

def add_fv(l_fv):
    #2.8.5
    for index,count in l_fv:
        weight[index] += count
        tmp_weight[index] += count*nupdates

def sub_fv(l_fv):
    #2.8.5
    for index,count in l_fv:
        weight[index] -= count
        tmp_weight[index] -= count*nupdates

def mult_fv(l_fv,weight):
    #2.8.6
    mult = 0
    for index,count in l_fv:
        if index > train_max:
            continue
        mult += weight[index] * count
    return mult

def averaged_weight(nupdates):
    local_ave_weight = [weight[i] - tmp_weight[i]/(nupdates+1) for i in range(len(weight))]
    return local_ave_weight

def update_weight(train_data,nupdates):
    #random.shuffle(train_data)
    rand = [i for i in range(len(train_data))]
    random.shuffle(rand)
    train_shuffled = [train_data[i] for i in rand]
    #train_data = train_shuffled

    for label,l_fv in train_shuffled:
        mult = mult_fv(l_fv,weight)
        if(mult*label <= options.margin):
            if(label > 0):
                add_fv(l_fv)
            else:
                sub_fv(l_fv)
        nupdates+=1
    if(options.average==True):
        ave_weight = averaged_weight(nupdates)
    else:
        ave_weight = []
    return train_shuffled,nupdates,ave_weight

def evaluate(test_data,weight):
    count = 0
    correct = 0
    for label,l_fv in test_data:
        mult = mult_fv(l_fv,weight)
        count += 1
        if(mult * label > 0):
            correct += 1
    return correct,count,correct/count

if __name__ == "__main__":
    #add options(2.9.9)
    usage = "usage: %prog [options] keyword"
    p = OptionParser(usage)
    p.add_option('-u',dest='update',default='1000',type='int',help='Num of times (updating)')
    p.add_option('-b',dest='bias',default='False',action='store_true',help='set bias terms')
    p.add_option('-n',dest='normalize',default='False',action='store_true',help='normalize the weight by L2 Norm')
    p.add_option('-m',dest='margin',default='0',type='float',help='set the margin')
    p.add_option('-a',dest='average',default='False',action='store_true',help='evaluate by averaged weight')
    options,args = p.parse_args()

    start = time.time()
    train_data,train_max = read_data(sys.argv[1])
    test_data,test_max = read_data(sys.argv[2])
    #2.8.4
    weight = [0]*(train_max+1)

    tmp_weight = [0]*(train_max+1)
    nupdates = 1

    random.seed(0)

    for i in range(options.update):
        train_data,nupdates,ave_weight = update_weight(train_data,nupdates)

    if(options.average==True):
        correct,count,accuracy = evaluate(test_data,ave_weight)
    else:
        correct,count,accuracy = evaluate(test_data,weight)
    print('correct'.ljust(9),':',correct)
    print('count'.ljust(9),':',count)
    print('accuracy'.ljust(9),':',accuracy)
    elapsed_time = time.time() - start

    print('time'.ljust(9),':',elapsed_time)

