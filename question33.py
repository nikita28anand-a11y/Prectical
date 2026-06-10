l = [2,6,8,-1,-6,-8]
pos = 0
neg = 0
for i in l:
    if i<0:
        neg=neg+1
    else:
        pos=pos+1
print(pos,neg)