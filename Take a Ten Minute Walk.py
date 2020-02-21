
# You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an
# appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk 
# Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing 
# directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block in a direction and you know it takes you
# one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you
# exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false
#                      otherwise.

# Note: you will always receive a valid array containing a random assortment of direction letters 
#                      ('n', 's', 'e', or 'w' only). It will never give you an empty array
#                      (that's not a walk, that's standing still!).


#best version:

def isValidWalk(walk):
    if (walk.count('n') == walk.count('s') and 
        walk.count('e') == walk.count('w') and
        len(walk) == 10):
            return True
    return False


#My version
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
