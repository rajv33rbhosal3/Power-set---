import math
def PPS(set,set_size):
    pss = (int)(math.pow(2,set_size))
    o = 0
    i = 0
    for o in range(0,pss):
        for i in range(0,set_size):
            if o & (1<<i)>0:
                print(set[i],end = "")
        print(" ")
size = int(input("Enter a number : "))
set = []
for a in range(0,size):
    n = int(input("Enter a element : "))
    set.append(n)
PPS(set,len(set))
