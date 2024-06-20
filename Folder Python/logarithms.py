# Bases for Logarithms
def f002 (L):
    newlist = []
    for i in L: # Loops n times
        if i % 2 == 0: # i
            newlist.append(i) # i (append is constant time on lists)
    return newlist # i return

f002([10,20,30,40,50])