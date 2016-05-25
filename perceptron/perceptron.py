import sys

def read_instance(review):
    #2.8.1
    l_line = review.strip().split(" ")
    l_fv = []
    label= l_line[0]
    del l_line[0]
    for fv in l_line:
        elem = fv.split(":")
        elem[0] = int(elem[0])
        elem[1] = float(elem[1])
        elem = tuple(elem)
        l_fv.append(elem)
    return (label,l_fv)

def read_data(data):
    #2.8.2
    l_instance = []
    v_max = 0
    for review in open(data,'r').readlines():
        instance = read_instance(review)
        l_instance.append(instance)
        #2.8.3
        for fv in instance[1]:
            if int(fv[0]) > int(v_max):
                v_max = int(fv[0])
    return l_instance,v_max

def add_fv(fv):
    #2.8.5
    for v in fv:
        weight[v[0]] += v[1]

def sub_fv(fv):
    #2.8.5
    for v in fv:
        weight[v[0]] -= v[1]

def mult_fv(fv):
    #2.8.6
    mult = 0
    for v in fv:
        if(max_index < v[0]):
            continue
        mult += weight[v[0]] * v[1]
    return mult

if __name__ == "__main__":
    train_data,max_index = read_data(sys.argv[1])
    
    #2.8.4
    weight = [0]*(max_index+1)
    
    for instance in train_data:
        lavel, fv = instance
        add_fv(fv)
        print(mult_fv(fv))
    print(weight)
          
