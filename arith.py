def arithEq(eq):
    return eval(eq)
def arithIneq( eq):
    res = 0
    symbol=0
    for i in range (len(eq)):
            if(eq[i]=='='):
                symbol=1
                lhs=eq[0:i]
                rhs=eq[i+1:]
                break
            elif(eq[i]=='>'):
                symbol=2
                lhs=eq[0:i]
                rhs=eq[i+1:]
                break
            elif(eq[i]=='<'):
                symbol=3
                lhs=eq[0:i]
                rhs=eq[i+1:]
                break
    if(symbol==1):
        if(arithEq(lhs)==arithEq(rhs)):
            res=1
    elif(symbol==2):
        if(arithEq(lhs)>arithEq(rhs)):
            res=1
    else:
        if(arithEq(lhs)<arithEq(rhs)):
            res=1
    return res

