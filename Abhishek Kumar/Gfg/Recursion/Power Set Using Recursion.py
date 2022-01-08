def powerSet(s,current='', i=0, subset=[]):
    if i == len(s):
        subset.append(current)
        return
    powerSet(s,current,i+1)
    powerSet(s,current+s[i],i+1)
    
    return subset
