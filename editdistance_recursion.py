import time
a=time.time()

def edDistRecursiveMemo(x,y,memo=None):
    if memo is None:memo={}        
    if len(x)==0: return len(y)
    if len(y)==0: return len(x)
    if(len(x),len(y)) in memo:
        return    memo[(len(x),    len(y))]
    delt = 1 if x[-1]!=y[-1] else    0
    diag = edDistRecursiveMemo(x[:-1],y[:-1],memo)+delt
    vert = edDistRecursiveMemo(x[:-1],y,memo)+1
    horz = edDistRecursiveMemo(x,y[:-1],memo)+1
    ans  = min(diag,vert,horz)
    memo[(len(x),len(y))]=ans
    return ans
    
def Main():
    target=raw_input("Target:")
    source=raw_input("Source:")
    print edDistRecursiveMemo(target,source)
    b=time.time()
    print "total time:",round((b-a),3)
    
    
if __name__=="__main__":
    Main()
