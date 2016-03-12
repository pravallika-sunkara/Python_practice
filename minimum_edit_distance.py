import time
a=time.time()

def editdistance(x,y):
    if(len(x)==0):
        return len(y)
    elif(len(y)==0):
        return len(x)
    delt=1 if x[-1] !=y[-1] else 0
    
    change=editdistance(x[:-1],y[:-1])+delt
    remove=editdistance(x[:-1],y)+1
    add=editdistance(x,y[:-1])+1
    return min(add,remove,change)
    
def Main():
    target=raw_input("Target:")
    source=raw_input("Source:")
    print editdistance(target,source)
    b=time.time()
    print round((b-a),3)
    
if __name__=="__main__":
    Main()
