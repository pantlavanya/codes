#Find Combinations of 2 Lists
def combinations(l,n):
    res = []
    for item in l[n]:
        if(n == len(l)-1):
            res.append(item)
        else:
            combos = combinations(l,n+1)
            for comb in combos:
                res.append([item,comb])
    return res

l = [[1,2],[3,4]]   #Output [[1,2],[1,3],[2,3],[2,4]]
result = combinations(l,0)
print result
