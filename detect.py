def isArith(eq):
    for i in range(len(eq)):
        if(eq[i].isalpha()):
            return False
    return True
def isArithEq(eq):
    for i in range(len(eq)):
        if((eq[i]=='=')or(eq[i]=='>')or(eq[i]=='<')):
            if(eq[-1]=='='):
                eq=eq[:-1]
                return True
            else:
                return False
    return True
