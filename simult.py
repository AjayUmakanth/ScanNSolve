from quad import coeff
import numpy as np
from graph import graph,addpts
def simult(eq,var,n):
    eq=eq.split('\n')
    A=[]
    B=[]
    for eqn in eq:
        vect,const=getvectors(eqn,var,n)
        A.append(vect)
        B.append(const)
    A=np.array(A)
    B=np.array(B)
    C=np.linalg.solve(A,B)
    Y=[]
    xpts=np.linspace(-C[0]-2,C[0]+2,10)
    for d,c in zip(A,B):
        a=d[0]
        b=d[1]
        y=list(map(lambda x:(c-a*x)/b,xpts))
        Y.append(y)
    addpts([C[0]],[C[1]])
    graph(xpts,Y,eq,"Simultaneous Equations")
    return (str(f"\t\t{var[0]}={round(C[0],3)}\n\t\t{var[1]}={round(C[1],3)}"))   

def getvectors(eq,var,n):
    vect=np.zeros(n)
    const=0
    s=0  #starting index of term
    sign=1
    term=""
    for i in range(len(eq)):
        if(i==0 and eq[i]=='-'):##checks if number is negative i.e., first character is -
            i+=1
        if(eq[i] == '+' or eq[i] == '-' or eq[i] == '=' or i == len(eq)-1):#enters the block only if end of a term is reached
            e=i  #ending index of term
            if i == len(eq)-1:#includes last character if character is last index of the equation
                e=i+1 
            if(eq[s] == '+' or  eq[s] == '=' ):# skip the character
                        s+=1
            for j in range(s,e):
                term+=eq[j]
            s=i
            cof=(sign*coeff(term))
            if(term[-1].isalpha()):
                ind=var.index(term[-1])
                vect[ind]+=cof
            else:
                const+=cof
            if(eq[i]=='='):
                sign=-1
            term=""
    return vect,const*-1

