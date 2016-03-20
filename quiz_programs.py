import math
feature = [2.5,.3,2.8,.5]
sentiment = [1,-1,1,1]
likelyhood = 1
loglikelyhood = 0
for x,y in zip(feature,sentiment):
    p=(1.0/(1+math.exp(-x)))
    loglikelyhood = loglikelyhood+x*((y == 1) - p)
    if y== -1:
        p = 1 - p
    print p
    likelyhood = likelyhood*p

print likelyhood
print loglikelyhood
