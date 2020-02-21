







def is_valid_walk(walk):
    #determine if walk is valid
    
    if len(walk) > 10:
        print("wrong2")
        return False
    length=len(walk)
    print(length )
    if length < 9:
        print(length,"Worng" )
        return False
    n=0
    s=0
    e=0
    w=0
    
    c=0
    i=1
    if walk[0] == 'n':
        n+=1
    elif walk[0]=='s':
        s+=1
    elif walk[0]=='e':
        e+=1
    else:
        w+=1
    print(walk[i],i,"n:",n,"s:",s,"e:",e,"w:",w)
    while i<length:
        if walk[i] == 'n':
            n+=1
        elif walk[i]=='s':
            s+=1
        elif walk[i]=='e':
            e+=1
        else:
            w+=1
        print(walk[i],i,"n:",n,"s:",s,"e:",e,"w:",w)
        i+=1
       
    print(n-s,w-e)
    if (n-s==0 and w-e==0):
        return True
        
    print("y")
    return False
