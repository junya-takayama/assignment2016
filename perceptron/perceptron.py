import sys

def read_instance(review):
    #2.8.1
    l_line = review.strip().split(" ")
    l_fv = []
    label= l_line[0]
    del l_line[0]
    for fv in l_line:
        elem = tuple(fv.split(":"))
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
                v_max = fv[0]
    return l_instance,v_max

if __name__ == "__main__":
    print(read_data(sys.argv[1]))
