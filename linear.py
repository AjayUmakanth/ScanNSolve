from arith import arithEq
import numpy as np
from graph import graph
def linear(eq,x):
    eqn=eq
    f0=""
    f1=""
    g0=""
    g1=""
    k=0
    for i in range(len(eq)):
        if(eq[i]=='='):
            k=1
            break
    if(not k):
        eq+='=0'
    i=0
    while eq[i]!='=':
        if(eq[i]!=x):
            f0+=eq[i]
            f1+=eq[i]
        else:
            if((eq[i-1]).isdigit() and i!=0):
                f0+='*'
                f1+='*'
                k+=1
            f0+='0'
            f1+='1'
            k+=1
        i+=1
    i+=1
    while i<len(eq):
        if(eq[i]!=x):
            g0+=eq[i]
            g1+=eq[i]
        else:
            if(isdigit(eq[i-1])):
                g0+='*'
                g1+='*'
                k+=1
            g0+='0'
            g1+='1'
            k+=1
        i+=1
    num=(arithEq(f0)-arithEq(g0))
    den=(arithEq(f0)-arithEq(g0)-arithEq(f1)+arithEq(g1))
    res=round(num/den,2)
    xpts=np.linspace(-10,10,1000)
    ypts=list(np.array(res*np.ones(len(xpts))))
    if(x=='x' or x=='X'):
        graph(ypts,[xpts],[eqn],"Linear Equations")
    if(x=='y' or x=='Y'):
        graph(xpts,[ypts],[eqn],"Linear Equations")
    return f"\t\t{x} = {res}\n"
